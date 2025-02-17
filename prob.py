def second_highest(lst):
    '''
    second_highest iterarte the list and give us the second highest number in the list 
    '''
    try:
        if len(lst) < 2:
            return "length of list should be more than two"
        first,second = 0,0
        for num in lst:
            if num > first:
                first,second = num,first
            elif second < num < first:
                second = num
        return second
    except Exception as e:
        return f"Error: {e}"

def main (): 
    '''
    function having list and calling the second_highest function
    '''
    try:
        my_list = []
        len=int(input("Enter the length of list: "))
        for i in range(len):
            num=int(input("Enter the number: "))
            my_list.append(num)
        print(f"List is: {my_list}")
        print(f"Second highest number in the list is: {second_highest(my_list)}")
    except Exception as e:
        return f"Error: {e}"
    
if __name__ =="__main__":
    main()
