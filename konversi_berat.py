def konversi_berat():
    try:
        berat = float(input("Masukkan berat: "))
    except ValueError:
        print("Masukkan angka yang valid.")
        return

    unit = input("Masukkan satuan berat (lb/kg): ").lower()

    if unit == "lb":
        berat_kg = berat * 0.453592
        print(f"{berat} pound setara dengan {berat_kg} kilogram.")
    elif unit == "kg":
        berat_lb = berat / 0.453592
        print(f"{berat} kilogram setara dengan {berat_lb} pound.")
    else:
        print("Masukkan satuan berat yang valid (lb/kg).")

if __name__ == "__main__":
    konversi_berat()
