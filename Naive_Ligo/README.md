# Naive Bayes Classifier: "Maligo" Decision Model

This project implements a **Multinomial Naive Bayes** approach to predict whether an individual will take a bath (**Maligo**) based on environmental and personal factors.

---

### Project Overview

The model analyzes historical data to calculate the probability of a "Yes" or "No" decision. It uses **Bayes' Theorem**, which determines the probability of an event based on prior knowledge of conditions related to that event.

### How the Algorithm Works

The classifier treats every feature (Weather, Time, Temperature, and Body Odor) as **independent**. To make a prediction, it calculates two main components:

1. **Prior Probability:** The general likelihood of "Yes" or "No" in the entire dataset.
* $P(\text{Yes}) = \frac{\text{Total Yes}}{\text{Total Records}}$


2. **Likelihood:** The probability of a specific condition (e.g., "Rainy") occurring given that the decision was "Yes."
* $P(\text{Rainy} \mid \text{Yes}) = \frac{\text{Count of Rainy Yes}}{\text{Total Yes}}$



---

### Dataset & Execution Example

The following data was used to train and test the model:

#### Input Data:

| ID | Weather | Time | Temperature | Body Odor | Maligo |
| --- | --- | --- | --- | --- | --- |
| 0 | Rainy | Morning | Cold | Fresh | No |
| 1 | Sunny | Noon | Hot | Smelly | Yes |
| 2 | Cloudy | Afternoon | Mild | Neutral | Yes |
| 3 | Sunny | Morning | Hot | Smelly | Yes |
| 4 | Rainy | Evening | Cold | Fresh | No |
| 5 | Sunny | Afternoon | Hot | Smelly | Yes |
| 6 | Cloudy | Morning | Mild | Neutral | Yes |
| 7 | Rainy | Noon | Cold | Smelly | Yes |
| 8 | Sunny | Evening | Mild | Fresh | No |
| 9 | Cloudy | Afternoon | Cold | Neutral | No |
| 10 | Rainy | Evening | Cold | Smelly | Yes |

#### Model Prediction Output:

For the scenario: **Rainy + Afternoon + Hot + Neutral**

* **Probability (YES):** `0.8181818181818181`
* **Probability (NO):** `0.36363636363636365`

### Final Conclusion

Since the probability for **YES** (0.818) is higher than the probability for **NO** (0.363), the model concludes that **the person will take a bath (Maligo)** under these circumstances.

---

### Technical Note: Calculation Method

In a standard Naive Bayes implementation, individual likelihoods are typically **multiplied** to find the joint probability. In this current logic, an additive approach is used to compare the relative weights of each feature.

**Key Drivers Found:**

* **Strongest Predictors:** "Hot" temperature and "Smelly" body odor are the strongest indicators for a **Yes** decision.
* **Negative Drivers:** "Fresh" body odor and "Cold" weather are the most common reasons for a **No** decision.

---