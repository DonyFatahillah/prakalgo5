print("\n \n")

print("@@@@   @@@@@   @@  @  @   @")
print("@   @  @   @   @ @ @   @ @")
print("@   @  @   @   @  @@    @")
print("@@@@   @@@@@   @   @    @")

print("\n \n")

jumlahLoop = int(input("Masukan Jumlah Bilangan : "))
firstNumber = int(input("Masukan Angka Pertama : "))
secondNumber = int(input("Masukan Angka Kedua : "))

deretFibonacci = [firstNumber, secondNumber]

for i in range(2, jumlahLoop):
    nextFibonacci = deretFibonacci[i-1]  + deretFibonacci[i-2]
    deretFibonacci.append(nextFibonacci)


for angka in deretFibonacci:
    print(f"Berikut Urutannya \n {angka}")
