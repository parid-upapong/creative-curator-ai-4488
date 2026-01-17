import xgboost as xgb
import optuna
from sklearn.model_selection import train_test_split
from sklearn.metrics import average_precision_score, roc_auc_score
import joblib
from .config import TrainingConfig
from .feature_engineering import preprocess_training_data

class EmploymentSuccessTrainer:
    def __init__(self, data_path: str):
        self.raw_df = pd.read_csv(data_path)
        self.config = TrainingConfig()
        
    def objective(self, trial):
        # Hyperparameter search space
        param = {
            'verbosity': 0,
            'objective': 'binary:logistic',
            'eval_metric': 'auc',
            'lambda': trial.suggest_float('lambda', 1e-8, 1.0, log=True),
            'alpha': trial.suggest_float('alpha', 1e-8, 1.0, log=True),
            'max_depth': trial.suggest_int('max_depth', 3, 9),
            'eta': trial.suggest_float('eta', 1e-3, 0.1, log=True),
            'gamma': trial.suggest_float('gamma', 1e-8, 1.0, log=True),
            'colsample_bytree': trial.suggest_float('colsample_bytree', 0.3, 0.9),
        }

        # Train/Test Split
        df = preprocess_training_data(self.raw_df)
        X = df.drop(columns=[self.config.TARGET])
        y = df[self.config.TARGET]
        
        train_x, valid_x, train_y, valid_y = train_test_split(
            X, y, test_size=self.config.TEST_SIZE, random_state=self.config.SEED
        )

        dtrain = xgb.DMatrix(train_x, label=train_y)
        dvalid = xgb.DMatrix(valid_x, label=valid_y)

        # Train model
        bst = xgb.train(param, dtrain)
        preds = bst.predict(dvalid)
        
        # Calculate Metric: PR-AUC is better for imbalanced hiring data
        score = average_precision_score(valid_y, preds)
        return score

    def run_training(self):
        print("🚀 Starting Hyperparameter Optimization for Employment Success...")
        study = optuna.create_study(direction='maximize')
        study.optimize(self.objective, n_trials=self.config.N_TRIALS)

        print(f"✅ Best Trial: {study.best_trial.value}")
        print(f"📊 Best Params: {study.best_params}")

        # Final Training with best params
        df = preprocess_training_data(self.raw_df)
        X = df.drop(columns=[self.config.TARGET])
        y = df[self.config.TARGET]
        
        final_model = xgb.XGBClassifier(**study.best_params)
        final_model.fit(X, y)

        # Save model for the Matching Service
        joblib.dump(final_model, self.config.MODEL_SAVE_PATH)
        print(f"💾 Model exported to {self.config.MODEL_SAVE_PATH}")

if __name__ == "__main__":
    trainer = EmploymentSuccessTrainer("data/historical_hiring_data.csv")
    trainer.run_training()