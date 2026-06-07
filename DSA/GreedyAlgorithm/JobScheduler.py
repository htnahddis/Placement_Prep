class Solution:
    def JobScheduling(self, Jobs, n):

        # Sort by profit descending
        Jobs.sort(key=lambda x: x[2], reverse=True)

        max_deadline = max(job[1] for job in Jobs)

        slots = [-1] * (max_deadline + 1)

        count = 0
        profit = 0

        for job in Jobs:

            job_id = job[0]
            deadline = job[1]
            curr_profit = job[2]

            # find latest free slot
            for j in range(deadline, 0, -1):

                if slots[j] == -1:
                    slots[j] = job_id
                    count += 1
                    profit += curr_profit
                    break

        return [count, profit]
    
    