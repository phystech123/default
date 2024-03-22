def foo(i):
    return i**3 - i**2 + i + 0.25

def mnk(arr, foo) -> None:
    arr2=[]
    for i in arr:
        j = foo(i)
        arr2.append(j)

    with open("data.csv", "w") as f:
        for i in range(len(arr)):
            f.write(f'{arr[i]}, {arr2[i]}\n')

def mnk2(arr, foo) -> None:
    arr2=[]
    for i in arr:
        j = foo(i)
        arr2.append(j)

    with open("MHK.txt", "w") as f:
        for i in range(len(arr)):
            f.write(f'{arr[i]}\t{arr2[i]}\n')



if __name__ == "__main__":
    arr=[
        x for x in range(21)
    ]
    mnk2(arr, foo)