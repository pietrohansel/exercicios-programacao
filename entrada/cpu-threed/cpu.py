class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:

        result = [0] * n  #cria uma lista con n elementos com valor 0
        stack = []
        prev_time = 0

        for log in logs:
            function_id, operation, timestamp = log.split(":")   #divide em uma lista com três elementos. Ex: ["1","start", "5" ]

            function_id = int(function_id)
            timestamp = int(timestamp)

            if operation == "start":
                if stack:
                    result[stack[-1]] += timestamp - prev_time # marcação atual do cronômetro - marcação a partir da qual você ainda precisa contabilizar o trabalho

                    stack.append(function_id)
                    prev_time = timestamp   # tempo a se contar, tornasse o tempo atual

            else:
                result[stack[-1]] += timestamp - prev_time + 1

                stack.pop(function_id)
                prev_time = timestamp + 1 

        return result
