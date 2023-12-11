open System 
open System.IO

let buildNumberLists (filepath: string) = 
    let lines = filepath |> File.ReadAllLines

    let splittedLines
        = lines 
            |> Array.map (fun line -> line.Split(" "))
            |> Array.map Array.toList
            |> Array.toList

    let mutable lists : int list list = []
    for l in splittedLines do 
        lists <- lists |> List.append [l |> List.map int] 

    lists <- lists |> List.rev 

    lists

    // printfn "Numbers:"
    // for l in lists do 
    //     for i in l do 
    //         printf "%i " i
    //     printfn ""
    //     printfn "-----------"


let extrapolateNextNumber (numberList: list<int>) = 
    let mutable currentList = numberList
    let mutable sum = 0

    while not(currentList |> List.forall (fun element -> element = 0)) do 
        let mutable nextList = []
        
        for i in 0..currentList.Length - 2 do
            nextList <- nextList |> List.append [currentList.[i+1] - currentList.[i]]
        nextList <- nextList |> List.rev    
        
        sum <- sum + currentList.[currentList.Length - 1]
        currentList <- nextList
    
    sum


let extrapolateBackwardNumber (numberList: list<int>) = 
    let mutable currentList = numberList
    let mutable firstNumbers = [numberList.[0]]
    let mutable extrapolateSteps = new System.Collections.Generic.Dictionary<int, int>()

    while not(currentList |> List.forall (fun element -> element = 0)) do 
        let mutable nextList = []
        
        for i in 0..currentList.Length - 2 do
            nextList <- nextList |> List.append [currentList.[i+1] - currentList.[i]]
        nextList <- nextList |> List.rev    
        
        firstNumbers <- firstNumbers |> List.append [nextList.[0]]
        currentList <- nextList

    for i in 0..firstNumbers.Length - 1 do 
        extrapolateSteps.Add(i, 0)
    
    firstNumbers <- firstNumbers |> List.rev

    for i in firstNumbers.Length - 2..-1..0 do 
        extrapolateSteps[i] <- firstNumbers.[i] - extrapolateSteps[i+1]

    extrapolateSteps.[0]


let sumAllExtrapolatedNumbers (numberLists: list<list<int>>) = 
    numberLists |> List.map (fun numberList -> numberList |> extrapolateNextNumber) |> List.sum

let sumAllExtrapolatedBackwardNumbers (numberLists: list<list<int>>) = 
    numberLists |> List.map (fun numberList -> numberList |> extrapolateBackwardNumber) |> List.sum

let fileIsGivenAndExists (arguments: String array) (filepath: string) = 
    arguments.Length = 1 && File.Exists filepath

[<EntryPoint>]
let main argv = 
    if argv.Length = 0 then 
        printfn "Please specify a file!"
        1
    elif argv.Length > 1 then
        printfn "More than one file given!"
        2
    else
        let filepath = argv.[0]
        if filepath |> fileIsGivenAndExists argv then 
            printfn "Processing %s" filepath

            let numberLists = filepath |> buildNumberLists

            let part1 = numberLists |> sumAllExtrapolatedNumbers
            let part2 = numberLists |> sumAllExtrapolatedBackwardNumbers
            printfn "Part 1: %i" part1
            printfn "Part 2: %i" part2 
            0
        else    
            printfn "File does not exist!"
            2   