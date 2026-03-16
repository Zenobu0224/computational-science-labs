# Naive Bayes Classifier: "Maligo" Decision Model

This project implements a **Multinomial Naive Bayes** approach to predict whether an individual will take a bath (**Maligo**) based on environmental and personal factors.

---

### Project Overview

The model analyzes historical data to calculate the probability of a "Yes" or "No" decision. It uses **Bayes' Theorem**, which determines the probability of an event based on prior knowledge of conditions related to that event.

### How the Algorithm Works

The classifier treats every feature (Weather, Time, Temperature, and Body Odor) as **independent**. To make a prediction, it calculates two main components:

1. **Prior Probability:** The general likelihood of "Yes" or "No" in the entire dataset.
* *Example:* $P(\text{Yes}) = \frac{\text{Total Yes}}{\text{Total Records}}$


2. **Likelihood:** The probability of a specific condition (e.g., "Rainy") occurring given that the decision was "Yes."
* *Example:* $P(\text{Rainy} \mid \text{Yes}) = \frac{\text{Count of Rainy Yes}}{\text{Total Yes}}$



### Dataset Features

The model evaluates the following inputs to reach a conclusion:

* **Weather:** Rainy, Sunny, Cloudy
* **Time:** Morning, Noon, Afternoon, Evening
* **Temperature:** Cold, Hot, Mild
* **Body Odor:** Fresh, Smelly, Neutral

---

### Technical Note: Multiplication vs. Addition

In a standard Naive Bayes implementation, individual probabilities are **multiplied**, not added. This is because we are looking for the joint probability of all conditions being true at the same time.

**The Probability Formula:**


$$P(\text{Decision} \mid \text{Features}) \propto P(\text{Decision}) \times \prod P(\text{Feature}_i \mid \text{Decision})$$

> **Zero-Frequency Problem:** If a specific condition (like "Hot" for a "No" decision) never appears in the data, the probability becomes 0. In professional environments, we use **Laplace Smoothing** (adding 1 to all counts) to ensure the model remains functional even with missing combinations.

---

### Key Insights

* **Strongest Predictors:** "Hot" temperature and "Smelly" body odor are the strongest indicators for a **Yes** decision.
* **Negative Drivers:** "Fresh" body odor and "Cold" weather are the most common reasons for a **No** decision.

---

**Would you like me to provide the updated Python code that implements the multiplication logic and Laplace smoothing to match this professional standard?**