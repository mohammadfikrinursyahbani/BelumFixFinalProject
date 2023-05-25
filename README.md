# Diabetes Prediction
Dalam Repository ini kelompok kami yakni DATUM melakukan implementasi model beberapa model mcahine learning untuk prediksi penyakit diabetes.
Model machine learning dan deployment nya dapat diakses di :
- [Notebook](https://github.com/mohammadfikrinursyahbani/BelumFixFinalProject/blob/main/Fikri_Project_Diabetes%20copy.ipynb)
- [Deployment App](https://github.com/mohammadfikrinursyahbani/BelumFixFinalProject/blob/main/app.py)

## Insight EDA
1. Diabetes lebih menonjol pada wanita dengan lebih banyak kehamilan.
2. Konsentrasi glukosa plasma yang lebih tinggi terlihat pada wanita dengan diabetes.
3. Tingkat insulin yang lebih tinggi ditemukan pada wanita yang menderita diabetes.
4. Wanita dengan diabetes memiliki BMI lebih tinggi.
5. Wanita penderita diabetes memiliki nilai fungsi diabetes keturunan yang lebih tinggi yang menunjukkan kaitan dengan riwayat keluarga.
6. Usia memiliki peran penting, diabetes lebih menonjol pada wanita usia paruh baya hingga lanjut usia.
7. Ketebalan kulit tidak berperan penting dalam kemungkinan diabetes.

## Data Preprocessing
1. Imputation dilakukan menggunakan mean untuk data yang terdistribusi hampir normal (data glucose, blood pressure) dan median untuk data yang skewed (data skin thickness, bmi, insulin).


## Table Model
| Model Machine Learning | Split Data | Train Accuracy | Test Accuracy | Precision | Recall | F-1 Score |
| Logistic Regression | 80 : 20 | 78.2% | 75.3% | 75% | 77% | 75% |
| XGBoost | 80 : 20 | 90.9% | 85.1% | 84% | 85% | 84% |
| Support Vector Classifier | 80 : 20 | 83.4% |	79.9% |	79% |	81% |	79% |
| KNeighbours Classifier | 80 : 20 | 82.5% | 74.0% | 74% |	76% |	73% |
| Decision Tree Classifier | 80 : 20 | 86.2% |	85.1% |	84% |	86% |	84% |
| Stacking (Random Forest, Adaboost, Logistic Regression | 80 : 20 | 89.2% |	88.3%	| 87%	| 88%	| 87% |
| Logistic Regression | 70 : 30 | 81.2% |	76.6%	| 75% | 78%	| 76% |
| XGBoost | 70 : 30 | 91.1%	| 87.9%	| 86%	| 87%	| 83% |
| Support Vector Classifier | 70 : 30 | 86.8%	| 78.4%	| 76%	| 78%	| 77% |
| KNeighbours Classifier | 70 : 30 | 83.5% | 75.8% | 74%	| 76%	| 75% |
| Decision Tree Classifier | 70 : 30 | 88.8%	| 83.1%	| 81%	| 82%	| 82% |
| Stacking (Random Forest, Adaboost, Logistic Regression | 70 : 30 | 90.7%	| 83.1%	| 81%	| 83%	| 82% |
| Logistic Regression | 60 : 40 | 80.3%	| 79.5%	| 78%	| 81%	| 78% |
| XGBoost | 60 : 40 | 90.1%	| 89.3%	| 88%	| 88%	| 88% |
| Support Vector Classifier | 60 : 40 | 85.7% |	82.1%	| 80%	| 83%	| 81% |
| KNeighbours Classifier | 60 : 40 | 82.7%	| 76.0%	| 74%	| 77%	| 75% |
| Decision Tree Classifier | 60 : 40 | 86.7%	| 85.4%	| 83%	| 85%	| 84% |
| Stacking (Random Forest, Adaboost, Logistic Regression | 60 : 40 | 88.8%	| 87.0%	| 85%	| 87%	| 86% |


## Kesimpulan

