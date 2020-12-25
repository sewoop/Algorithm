// MARK: - Partitioning
func partition(data: inout [Int], start: Int, end: Int) -> Int {
    let pivot: Int = data[start]
    var L: Int = start
    var R: Int = end
    var temp: Int = 0
    
    while true {
        while L <= data.count - 1 && data[L] <= pivot {
            L += 1
        }
        
        while R >= 0 && data[R] > pivot {
            R -= 1
        }
        
        if R <= L {
            temp = data[start]
            data[start] = data[R]
            data[R] = temp
            break
        } else {
            temp = data[L]
            data[L] = data[R]
            data[R] = temp
        }
    }
    
    return R
}

// MARK: - QuickSort
func quickSort(data: inout [Int], start: Int, end: Int) -> [Int]{
    if start <= end {
        let pivot = partition(data: &data, start: start, end: end)
        quickSort(data: &data, start: start, end: pivot - 1)
        quickSort(data: &data, start: pivot + 1, end: end)
    }
    return data
}

var data = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
print(quickSort(data: &data, start: 0, end: data.count - 1))
