## Question 1

Take a look at the file labeled `data/phase0.txt`. Why might we have missing values or values that state "NO DATA" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

Missing data can result from various factors. Person(s) may take off the sensor, I know that network issues can cause downtime as well (wifi, bluetooth, etc...), and devices can also experience system errors, which can affect data collection. 

The risk of filtering: Pontentially valuable information about device, skewed results, etc.., could be overlooked, which may lead to incorrect results/analysis. 

## Question 2

During sleep, we expect maximum heart rate of a phase to be **lower** than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase does sleep occur? Mention numerical details that back your findings.

According to Phases 0 and 3 descriptive statistics, (64.59, 93, 8.53) and (60.65, 99, 11.0), we can see that there are comparatively low max values in relation to all other phases, which I believe, indicates sleep in both Phases. Phase3 however, has a higher spread which indicates a deeper more restful sleep in Phase0.

## Question 3

During exercise, we expect the maximum heart rate of a phase to be **higher** than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase(s) does exercise occur? Mention numerical details that back your findings. 

Phase2's descriptive statistics, (85.18, 117, 13.38), shows higher maximum heart rate compared to all other phases. Also the average and standard deviation shows elevated heart rate and high spread, respectively. The line graph clearly shows elevated heart rate between 100 and approximately 115 beats per minute (bpm) for nearly 30 mins. This may suggest cardio or an intense consistent exercise routine. We can also see a decrease in heart rate, which stays between about 70 to 100 bpm for the remaining 30 mins, which suggests an end to the exercise routine and the individual is at the standard wake time of 60-100 bpm (webmd.com). 

## Question 4

During regular periods of awake activity, we expect the average heart rate of a phase to be relatively **lower** than the average heart rate of other phases, but we also expect standard deviation to be **higher**. In which phase do we notice this trend?

According to Phase1's descriptive statistics, (87.3, 110, 9.9), we can see that the Max heart rate is 110 with a standard deviation of 9.9. Also according to the line chart, we can see even clearer that the maximum heart rate hovers around about 60 to slighlty higher than 100 bpm. This suggests "wake time" which is usually "between 60-100 bpm" (sleepfoundation.org); or normal awake time activities, such as lifting, walking, etc.., with the slightly higher spread of 9.9.  

Notes: Phases 0, 1, 2, and 3's descriptuve statistics (mean, max, and standard deviation), respectively:
Phase0 (64.59, 93, 8.53)
Phase1 (87.3, 110, 9.9)
Phase2 (85.18, 117, 13.38), and 
Phase3 (60.65, 99, 11.0)

Sources:
- sleepfoundation.org: Normal resting rate is typically between 60 and 100 bpm. A normal heart rate during sleep drops to between 40 and 50 bpm.
- Early detection of Heart rate anomallies can lead to beter overall heath and sleep quality.
- Webmd.com: Typical heart rate is normally between 60 and 100 bpm. 

