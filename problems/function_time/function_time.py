# Decagon phone screen.

from typing import List

# Example 1:
# input: ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
# output: [3, 4]
# Explanation: Function 0 runs for 3 time units [0, 1, 6], and function 1 runs for 4 time units [2, 3, 4, 5].

# Example 2:
# input: ["0:start:0", "1:start:2", "1:end:5", "2:start:7", "2:end:8", "0:end:9"]
# output: [4, 4, 2]
# Explanation: Function 0 runs for 4 time units [0, 1, 6, 9], function 1 runs for 4 time units [2, 3, 4, 5], and function 2 runs for 2 time units [7, 8].

# Example 3:
# input: ["0:start:0", "0:start:2", "0:end:5", "1:start:7", "0:start:8", "0:end:9", "1:end:10", "0:end:12"]
# output: [9, 3]
# Explanation: Function 0 runs for 9 time units [0, 1, 2, 3, 4, 5, 6, 8, 9, 12], recursively calling itself. Function 1 runs for 3 time units [7, 10, 11].


def calculate_function_time(logs: List[str]) -> List[int]:
    """
    Calculate the exclusive execution time for each function.

    Args:
        n: Number of functions (not used in this implementation)
        logs: List of log entries in format "function_id:start/end:timestamp"

    Returns:
        List of execution time for each function
    """
    stack = []  # Stack to track currently running functions with their start times
    result = {}  # Dictionary to store execution time for each function

    for log in logs:
        function_id, action, timestamp = log.split(":")
        function_id = int(function_id)
        timestamp = int(timestamp)

        if action == "start":
            # If there's a currently running function, pause its time
            if stack:
                current_function, start_time = stack[-1]
                result[current_function] += timestamp - start_time

            # Start the new function
            stack.append((function_id, timestamp))
            if function_id not in result:
                result[function_id] = 0

        else:  # action == "end"
            # Calculate execution time for the ending function
            current_function, start_time = stack.pop()
            execution_time = timestamp - start_time + 1
            result[current_function] += execution_time

            # If there are other functions in stack, resume their time
            if stack:
                # Update the start time of the function that was paused
                paused_function, _ = stack[-1]
                stack[-1] = (paused_function, timestamp + 1)

    # Convert to list format, sorted by function ID
    max_function_id = max(result.keys()) if result else 0
    output = []
    for i in range(max_function_id + 1):
        if i in result:
            output.append(result[i])
        else:
            output.append(0)

    return output


# Test cases
if __name__ == "__main__":
    # Test Example 1
    logs1 = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    result1 = calculate_function_time(2, logs1)
    print("Example 1:", result1)  # Expected: [3, 4]

    # Test Example 2
    logs2 = ["0:start:0", "1:start:2", "1:end:5",
             "2:start:7", "2:end:8", "0:end:9"]
    result2 = calculate_function_time(3, logs2)
    print("Example 2:", result2)  # Expected: [4, 4, 2]

    # Test Example 3
    logs3 = ["0:start:0", "0:start:2", "0:end:5", "1:start:7",
             "0:start:8", "0:end:9", "1:end:10", "0:end:12"]
    result3 = calculate_function_time(2, logs3)
    print("Example 3:", result3)  # Expected: [9, 3]
