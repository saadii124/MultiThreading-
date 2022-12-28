# Name : M.Saad Bin Shafiq
# Reg No: 200901079
# Batch: BSCS-01-B

import threading

def func1(num):
    print("\nShortest job first")

    class ShortJF:

        def processData(self, no_of_processes):
            process_data = []
            for i in range(no_of_processes):
                temporary = []
                process_id = int(input("Enter Process No for SJF: "))
                arrival_time = int(input(f"Enter Arrival Time of Process for SJF {process_id}: "))
                burst_time = int(input(f"Enter Burst Time of Process for SJF{process_id}: "))
                temporary.extend([process_id, arrival_time, burst_time, 0])

                process_data.append(temporary)
            ShortJF.schedulingProcess(self, process_data)

        def schedulingProcess(self, process_data):
            start_time = []
            exit_time = []
            s_time = 0
            process_data.sort(key=lambda x: x[1])

            for i in range(len(process_data)):
                ready_queue = []
                temp = []
                normal_queue = []

                for j in range(len(process_data)):
                    if (process_data[j][1] <= s_time) and (process_data[j][3] == 0):
                        temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                        ready_queue.append(temp)
                        temp = []
                    elif process_data[j][3] == 0:
                        temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                        normal_queue.append(temp)
                        temp = []

                if len(ready_queue) != 0:
                    ready_queue.sort(key=lambda x: x[2])

                    start_time.append(s_time)
                    s_time = s_time + ready_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    for k in range(len(process_data)):
                        if process_data[k][0] == ready_queue[0][0]:
                            break
                    process_data[k][3] = 1
                    process_data[k].append(e_time)

                elif len(ready_queue) == 0:
                    if s_time < normal_queue[0][1]:
                        s_time = normal_queue[0][1]
                    start_time.append(s_time)
                    s_time = s_time + normal_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    for k in range(len(process_data)):
                        if process_data[k][0] == normal_queue[0][0]:
                            break
                    process_data[k][3] = 1
                    process_data[k].append(e_time)

            t_time = ShortJF.calculateTurnaroundTime(self, process_data)
            w_time = ShortJF.calculateWaitingTime(self, process_data)
            ShortJF.printData(self, process_data, t_time, w_time)

        def calculateTurnaroundTime(self, process_data):
            total_turnaround_time = 0
            for i in range(len(process_data)):
                turnaround_time = process_data[i][4] - process_data[i][1]
                total_turnaround_time = total_turnaround_time + turnaround_time
                process_data[i].append(turnaround_time)
            average_turnaround_time = total_turnaround_time / len(process_data)
            return average_turnaround_time

        def calculateWaitingTime(self, process_data):
            total_waiting_time = 0
            for i in range(len(process_data)):
                waiting_time = process_data[i][5] - process_data[i][2]
                total_waiting_time = total_waiting_time + waiting_time
                process_data[i].append(waiting_time)
            average_waiting_time = total_waiting_time / len(process_data)

            return average_waiting_time

        def printData(self, process_data, average_turnaround_time, average_waiting_time):
            process_data.sort(key=lambda x: x[0])

            print("Processes  Arrival_Time  Burst_Time      Completed  Completion_Time  Turnaround_Time  Waiting_Time")

            for i in range(len(process_data)):
                for j in range(len(process_data[i])):
                    print(process_data[i][j], end="				")
                print()
            print(f'Average Turnaround Time: {average_turnaround_time}')
            print(f'Average Waiting Time: {average_waiting_time}')

    if __name__ == "__main__":
        no_of_processes = int(input("Enter number of processes for SJF: "))
        sjf = ShortJF()
        sjf.processData(no_of_processes)




def func2(num):
    print("FIRST COME FIRST SERVE")
    no_process = 0
    no_process = int(input("Enter no of processes for FCFS:"))
    process = []
    burst_time = []
    waiting_time = []
    turn_around_time = []
    # taking values
    for i in range(no_process):
        x = int(input("Enter Process for FCFS:"))
        process.append(x)
        y = int(input("Enter Burst Time of Process for FCFS: "))
        burst_time.append(y)

    # Printing values
    print()
    print("executing")

    x = 0
    waiting_time.append(x)
    for i in range(1, no_process):
        x = burst_time[i - 1] + waiting_time[i - 1]
        waiting_time.append(x)

    for i in range(0, no_process):
        x = burst_time[i] + waiting_time[i]
        turn_around_time.append(x)

    avgwt = 0
    avgtat = 0
    for i in range(0, no_process):
        avgwt = avgwt + waiting_time[i]
        avgtat = avgtat + turn_around_time[i]

    avgtat = avgtat / no_process
    avgwt = avgwt / no_process

    # printing Turn around Time and waiting
    print()
    for i in range(0, no_process):
        print("Process=", process[i])
        print("Burst Time=", burst_time[i])
        print("Waiting Time=", waiting_time[i])
        print("Turn Around Time=", turn_around_time[i])

    print()
    print("Average Waiting Time=", avgwt)
    print("Average Turn Around Time=", avgtat)


if __name__ == "__main__":
    t1 = threading.Thread(target=func2, args=(10,))
    t2 = threading.Thread(target=func1, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
