from dotenv import load_dotenv
from mem0 import MemoryClient
import logging
import json

# Load environment variables
load_dotenv()

# User ID
user_name = "mahi"

# Initialize Mem0 client
mem0 = MemoryClient()


def add_memory():

    messages_formatted = [
        {"role": "user", "content": "I really like Linkin Park."},
        {"role": "assistant", "content": "That is a good choice."},
        {"role": "user", "content": "I think so too."},
        {"role": "assistant", "content": "What is your favorite song by them?"},
        {"role": "user", "content": "I live in Hyderabad."},
        {"role": "assistant", "content": "Hyderabad is a great city."},
        {"role": "user", "content": "My favorite food is biryani."}
    ]

    # Add memory with categories
    mem0.add(
        messages_formatted,
        user_id=user_name,
        categories=["music", "location", "food"]
    )

    print("Memory added successfully!")


def get_memory_by_query():

    query = f"What are {user_name}'s preferences?"

    results = mem0.search(query, user_id=user_name)

    memories = [
        {
            "memory": result["memory"],
            "updated_at": result["updated_at"]
        }
        for result in results
    ]

    memories_str = json.dumps(memories, indent=2)

    print("Retrieved Memories:")
    print(memories_str)

    return memories_str


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    # Store memories
    add_memory()

    # Retrieve memories
    get_memory_by_query()