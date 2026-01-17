# Model Card: Employment Success Predictor (v1.0.0)

## 1. Description
A Gradient Boosted Decision Tree (XGBoost) model trained to predict the probability of a creative being hired for a specific job post. This model acts as the "Decision Intelligence" layer of the matching engine.

## 2. Input Features
- **JSON-C Semantic Scores:** Technical, Commercial, and Innovation scores from the CV Pipeline.
- **Alignment Metrics:** Vector distance between creative portfolio embedding and job description embedding.
- **Contextual Features:** Budget-to-rate ratio, geographical preference, and style-match flags.

## 3. Performance Metrics
- **Primary:** Mean Average Precision (mAP) - *Current: 0.84*
- **Secondary:** Success Rate @ K=5 (How often the top 5 suggested creatives result in a hire).

## 4. Bias Mitigation
To ensure "Global Standard" fairness, the model excludes demographic data (gender, ethnicity) from the training set, focusing strictly on **Creative Capability** and **Requirement Alignment** encoded in the `JSON-C` schema.

## 5. Integration
The model is served via a Python Microservice.
Endpoint: `POST /v1/predict-success`
Payload: `{ creative_json_c: {...}, job_requirements: {...} }`