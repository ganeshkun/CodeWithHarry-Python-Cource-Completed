def main():
    try:
       a = int(input("Hey, enter a number: "))
       print(a)

    except Exception as e:
      print(e)

    finally:
      print("i am inside finally")

main()