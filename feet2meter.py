def feet2meter(v):

    v = v.replace("ft", "")


    feet = float(v)


    meters = feet * 0.3048

    
    return meters

def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

if __name__ == '__main__':
    main()