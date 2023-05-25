# Gender Classification menggunakan VGG, ResNet and GoogleNet
Dalam Repository ini kelompok kami yakni Al Khwarizmi melakukan implementasi model beberapa model deep learning untuk klasifikasi jenis kelamin (gender) dengan datasets CelebA. Model Deep Learning yang kami coba implementasikan yakni:
- [VGG16](https://github.com/mohammadfikrinursyahbani/FaceClassificationByGender/blob/main/fix_face_classification.ipynb). (By Mohammad Fikri Nur Syahbani)
- [ResNet-18](https://github.com/mohammadfikrinursyahbani/FaceClassificationByGender/blob/main/ResNet.ipynb) (Take Over By Mohammad Fikri Nur Syahbani)
- [Google Net Inception v1](https://github.com/mohammadfikrinursyahbani/FaceClassificationByGender/blob/main/GoogleNet_Gender_Recognition_.ipynb). (By Slamet Mahendra)

## Strategi Implementasi Model
Dalam implementasi model di atas kami menggunakan beberapa kriteria untuk uji coba yakni:
1. Menguji scope Learning rate yakni 0.001, 0.01 dan 0.1
2. Menguji scope Batch size yakni 16, 32 dan 64 dengan menggunakan hasil learning rate terbaik
3. Menguji scope  Split data yakni 80:20, 70:30 dan 60:40 menggunakan hasil learning rate terbaik.

## Table Model
| Test Case | Learning rate | Epoch | Split data | Batch size | VGG16 | ResNet-18 | GoogleNet |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Learning rate 0.001 | 0.001 | 5 | 80:20 | 32 | 0.9221 | 0.7947 | 0.9016 |
| Learning rate 0.01 | 0.01 | 5 | 80:20 | 32 | 0.9221 | 0.7953 | 0.4873 |
| Learning rate 0.1 | 0.1 | 5 | 80:20 | 32 | 0.8859 | 0.7367 | 0.5127 |
| Batch_size 16 | 0.001 | 5 | 80:20 | 16 | 0.9348 | --- | 0.8539 |
| Batch_size 32 | 0.001 | 5 | 80:20 | 32 | 0.9336 | ---| 0.8225 |
| Batch_size 64 | 0.001 | 5 | 80:20 | 64 | 0.9245 | --- | 0.8478 |
| Split Data 80:20 | 0.001 | 20 | 80:20 | 16 | 0.9348 <br/>(stop in 11 epoch) | 0.8231 | **0.9589** |
| Split Data 70:30 | 0.001 | 20 | 70:30 | 16 | 0.9312 <br/>(stop in 12 epoch) | 0.7878 <br/>(stop in 12 epoch) | 0.9452 <br/>(stop in 19 epoch) |
| Split Data 60:40 | 0.001 | 20 | 60:40 | 16 | 0.9321 <br/>(stop in 5 epoch) | 0.8112 | 0.9493 |

## Kesimpulan
- Learning rate : Semakin kecil learning rate, loss functionya semakin kecil, namun untuk proses waktu training semakin lama
- Batch_size : Semakin besar, semakin cepat proses training, namun loss function semakin besar
- epoch : Semakin banyak semakin bisa untuk belajar atau training, namun ketika tidak ada perubahan pada akurasi tiap epoch nya, maka besar epoch tidak terlalu berimbas pada model
- split training test 80:20; 70:30; dan 60:40; : Tidak memberikan pengaruh yang signifikan pada akurasi model
- Arsitektur Model : Dalam hal ini model GoogleNet dengan learning rate 0.001, 80:20, batch size: 16 dan epoch 20 mendapatkan akurasi paling tinggi sebesar 0.9589.
