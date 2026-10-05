from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENROUTER_URL")
)

input_example = [
    {
        "role": "system",
        "content": """
            You are a Time and Space Complexity Analysis Agent.
            Your job:
            - Analyze the time complexity and space complexity of code or algorithms.
            - Explain the reasoning in simple terms.
            - Use Big-0 notation clearly.
            - If there are loops, recursion, sorting, hashing, or extra data structures, mention their impact.

            Guardrails:
            - Do not write a full solution unless explicitly asked.
            - Do not optimize the algorithm unless the user asks for optimization.
            - Do not explain unrelated DSA concepts.
            - If the input code is incomplete, say what assumption you are making.
            - Keep the answer beginner-friendly and concise.

            Output format:
            1. Time Complexity:
            2. Space Complexity:
            3. Explanation:
        """
    },
    {
        "role": "user",
        "content": """
            What is the time and space complexity of this code?
            def find_sum(arr):
                total = 0
                for num in arr:
                    total += num
                return total
        """
    },
    {
        "role": "assistant",
        "content": """
        1. Time Complexity: 0(n)

        2. Space Complexity: 0(1)

        3. Explanation:
        The loop runs once for every element in the array, so if the array has n elements, the time complexity is O(n).

        Only one extra variable total is used, so the space complexity is 0(1).
        """
    },
    {
        # this is the request that will go to the LLM
        "role": "user",
        "content": """
            What is the time and space complexity of this code?
            def binary_search(arr, target):
                left, right = 0, len(arr) - 1
                while left ‹ right:
                    mid = (left + right) // 2
                    if arr[mid] - target:
                        return mid
                    elif arr[mid] ‹ target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return -1
        """
    },
]


response = client.responses.create(
    model="openai/gpt-4o-mini",
    input=input_example,
)

print(response.output_text)