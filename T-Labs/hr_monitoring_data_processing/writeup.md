## Question 1

Take a look at the file labeled `data/phase0.txt`. Why might we have missing values or values that state "NO DATA" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

Missing data can result from various factors. Person(s) may take off the sensor, I know that network issues can cause downtime as well (wifi, bluetooth, etc...), and system errors with device. 

The risk of filtering: Pontentially valuable information about device, skewed results, etc.., could be overlooked, which may lead to incorrect results/analysis. 

## Question 2

During sleep, we expect maximum heart rate of a phase to be **lower** than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase does sleep occur? Mention numerical details that back your findings.

according to Phase0's output descriptive statistics, (64.59, 93, 8.53), we can see that 93 is the lowest max value of all other phases--although only by 6. Phase0's average and standard deviation is also pretty low--although phase1's standard deviation is also competitively low. This suggest with Phase0 that most values are close dispersed about the mean of 64.59. This tells me sleep or resting state. 

## Question 3

During exercise, we expect the maximum heart rate of a phase to be **higher** the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase(s) does exercise occur? Mention numerical details that back your findings. 

[Answer here]

## Question 4

During regular periods of awake activity, we expect the average heart rate of a phase to be relatively **lower** than the average heart rate of other phases, but we also expect standard deviation to be **higher**. In which phase do we notice this trend?

[Answer here]

Notes: Phases 0, 1, 2, and 3's descriptuve statistics (mean, max, ans standard deviation), respectively:
Pase0 (64.59, 93, 8.53)
Phase1 (87.3, 110, 9.9)
Phase2 (85.18, 117, 13.38), and 
Phase3 (60.65, 99, 11.0)
