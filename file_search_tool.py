from typing import Dict, List, Union
from openai import OpenAI


def create_file_search_function(client: OpenAI, file_paths: List[str]):
    """Create a file search function with a vector store bound to the provided files.

    Args:
        client: OpenAI client instance
        file_paths: List of file paths to add to the vector store

    Returns:
        A file_search function with the vector store already configured
    """
    # Create vector store
    vector_store = client.vector_stores.create(name="file_search_store")

    # Upload files to the vector store
    file_streams = []
    try:
        for file_path in file_paths:
            with open(file_path, "rb") as f:
                file_streams.append(f)
                # Upload file
                file_obj = client.files.create(file=f, purpose="assistants")
                # Add file to vector store
                client.vector_stores.files.create(
                    vector_store_id=vector_store.id, file_id=file_obj.id
                )
    except Exception as e:
        # Clean up vector store if file upload fails
        try:
            client.vector_stores.delete(vector_store.id)
        except Exception:
            pass
        raise e

    def file_search(query: str) -> Dict[str, Union[str, List[str]]]:
        """Search through uploaded files using vector search.

        Args:
            query: The search query to find relevant content in the files

        Returns:
            Dict containing:
                - query: The original search query
                - results: List of relevant text snippets from the files
                - sources: List of source file names where results were found
        """
        try:
            # Use vector store search to find relevant content
            search_results = client.vector_stores.search(
                vector_store_id=vector_store.id, query=query
            )

            results = []
            sources = []

            # Iterate through search results
            for result in search_results:
                # Add filename to sources if not already present
                if hasattr(result, "filename") and result.filename:
                    if result.filename not in sources:
                        sources.append(result.filename)

                # Extract text content from content chunks
                if hasattr(result, "content") and result.content:
                    for content_chunk in result.content:
                        if hasattr(content_chunk, "text") and content_chunk.text:
                            results.append(content_chunk.text)

            return {
                "query": query,
                "results": results if results else ["No relevant content found"],
                "sources": sources,
            }

        except Exception as e:
            return {
                "query": query,
                "results": [f"Error during search: {str(e)}"],
                "sources": [],
            }

    # Store vector store ID on the function for cleanup
    file_search._vector_store_id = vector_store.id
    file_search._client = client

    return file_search


def cleanup_file_search_function(file_search_func):
    """Clean up the vector store associated with a file search function.

    Args:
        file_search_func: The file search function returned by create_file_search_function
    """
    if hasattr(file_search_func, "_vector_store_id") and hasattr(
        file_search_func, "_client"
    ):
        try:
            file_search_func._client.vector_stores.delete(
                file_search_func._vector_store_id
            )
        except Exception as e:
            print(f"Warning: Failed to cleanup vector store: {e}")
