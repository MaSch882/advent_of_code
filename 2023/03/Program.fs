open System
open System.IO

let numbers = ["0";"1"; "2"; "3"; "4"; "5"; "6"; "7"; "8"; "9"]
let delimiter = "."
let gear = "*"

let buildMatrixFromInput (filepath: string) =
     filepath 
     |> File.ReadAllLines 
     |> Seq.toList 
     |> List.map (fun line -> line.ToCharArray()) 
     |> Seq.toList

let isRelevantPartNumber (s: string) =
    (not (List.contains s numbers)) && s <> delimiter

let checkEntry (i: int) (j: int) (matrix: char array list) =
    try
        if isRelevantPartNumber (string matrix.[i].[j]) then
            true
        else 
            false
    with
        _ -> false 

let isRelevantNumber (i: int) ( j: int) (matrix: char array list)  = 
    // links oben
    if matrix |> checkEntry (i-1) (j-1) then 
        true
    // links
    elif matrix |> checkEntry i (j-1)  then 
        true
    // links unten 
    elif matrix |> checkEntry (i+1) (j-1) then 
        true
    // oben
    elif matrix |> checkEntry (i-1) j then
        true
    // unten 
    elif matrix |> checkEntry (i+1) j then 
        true
    // rechts oben
    elif matrix |> checkEntry (i-1) (j+1) then 
        true
    // rechts
    elif matrix |> checkEntry i (j+1) then 
        true 
    // rechts unten
    elif matrix |> checkEntry (i+1) (j+1) then 
        true
    else 
        false 



let sumAllPartNumbers (matrix: char array list) = 
    let mutable sumOfPartNumbers = 0

    for i in 0..matrix.Length - 1 do
        let mutable currentNumber = ""
        let mutable isRelevant = false

        for j in 0..matrix.[0].Length - 1 do
            let currentChar = string(matrix.[i].[j])            

            // Ist currentChar eine Zahl? Dann an currentNumber appenden.
            let isCurrentCharANumber = List.contains currentChar numbers
            if isCurrentCharANumber then
                currentNumber <- String.Concat([currentNumber; currentChar])
            
            // Falls gerade eine relevante Zahl am Zeiger ist, wird isRelevant auf true gesetzt.
            if isCurrentCharANumber && matrix |> isRelevantNumber i j then
                isRelevant <- true

            // Ist die Zahl zu Ende?
            try 
                // Zahl zu Ende
                if not (List.contains (string(matrix.[i].[j+1])) numbers) then 
                    // Falls die Zahl relevant ist, summieren wir.
                    if isRelevant then
                        sumOfPartNumbers <- sumOfPartNumbers + int(currentNumber)
                        currentNumber <- ""
                        isRelevant <- false
                    else 
                        currentNumber <- ""
                        isRelevant <- false
            with 
                // In diesem Fall ist in der if-Abfrage eine IndexOutOfRangeException geflogen.
                // Dies ist äquivalent dazu, dass wir am rechten Rand der Matrix stehen.
                // Daher tun wir hier nichts und pruefen diesen Fall einzeln ab.
                _ -> ()
            
            // Sind wir am rechten Rand der Matrix und unser letztes Zeichen ist eine Ziffer einer relevanten Zahl?
            if j = matrix.[0].Length - 1 && List.contains currentChar numbers && isRelevant then
                sumOfPartNumbers <- sumOfPartNumbers + int(currentNumber)
                currentNumber <- ""
                isRelevant <- false
    sumOfPartNumbers

let isGear (i: int) (j: int) (matrix: char array list) =
    if string matrix.[i].[j] <> gear then 
        false 
    else 
        false


let calculateGearRatio (matrix: char array list) (i: int) (j: int) = 
    0

let sumAllGearRatios (matrix: char array list) =
    let mutable sumOfGearRatios = 0
    
    for i in 0..matrix.Length - 1 do 
        for j in 0..matrix.[0].Length - 1 do 
            if matrix |> isGear i j then 
                printfn "Gear found at (%i, %i)" i j
                let gearRatio = calculateGearRatio matrix i j
                sumOfGearRatios <- sumOfGearRatios + gearRatio
            else 
                ()

    sumOfGearRatios


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
            let part1 = filepath |> buildMatrixFromInput |> sumAllPartNumbers            
            let part2 = filepath |> buildMatrixFromInput |> sumAllGearRatios
            printfn "Part 1: %i" part1
            printfn "Part 2: %i" part2
            0
        else    
            printfn "File does not exist!"
            2   