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

let countAdjacentNumbers (i: int) (j: int) (matrix: char array list) = 
    let mutable adjacentNumbers = 0

    let upLeft = string matrix.[i-1].[j-1]
    let up = string matrix.[i-1].[j]
    let upRight = string matrix.[i-1].[j+1]

    let belowLeft = string matrix.[i+1].[j-1]
    let below = string matrix.[i+1].[j]
    let belowRight = string matrix.[i+1].[j+1]
    
    let left = string matrix.[i].[j-1]
    let right = string matrix.[i].[j+1]

    // Rechts und links vom *
    if numbers |> List.contains left then
        adjacentNumbers <- adjacentNumbers + 1
    if numbers |> List.contains right then 
        adjacentNumbers <- adjacentNumbers + 1

    // Oben vom *
    if numbers |> List.contains up then
        adjacentNumbers <- adjacentNumbers + 1
    elif numbers |> List.contains upLeft && numbers |> List.contains up then 
        adjacentNumbers <- adjacentNumbers + 1
    elif numbers |> List.contains upRight && numbers |> List.contains up then 
        adjacentNumbers <- adjacentNumbers + 1
    elif numbers |> List.contains upRight && numbers |> List.contains upLeft && not (numbers |> List.contains up) then 
        adjacentNumbers <- adjacentNumbers + 2
    elif numbers |> List.contains upLeft && not (numbers |> List.contains up) && not (numbers |> List.contains upRight) then
        adjacentNumbers <- adjacentNumbers + 1
    elif numbers |> List.contains upRight && not (numbers |> List.contains up) && not (numbers |> List.contains upLeft) then
        adjacentNumbers <- adjacentNumbers + 1
    

    // Unten vom *
    if numbers |> List.contains below then
        adjacentNumbers <- adjacentNumbers + 1
    elif numbers |> List.contains belowLeft && numbers |> List.contains below then 
        adjacentNumbers <- adjacentNumbers + 1
    elif numbers |> List.contains belowRight && numbers |> List.contains below then 
        adjacentNumbers <- adjacentNumbers + 1
    elif numbers |> List.contains belowRight && numbers |> List.contains belowLeft && not (numbers |> List.contains below) then 
        adjacentNumbers <- adjacentNumbers + 2
    elif numbers |> List.contains belowLeft && not (numbers |> List.contains below) && not (numbers |> List.contains belowRight) then
        adjacentNumbers <- adjacentNumbers + 1
    elif numbers |> List.contains belowRight && not (numbers |> List.contains below) && not (numbers |> List.contains belowLeft) then
        adjacentNumbers <- adjacentNumbers + 1

    adjacentNumbers

let isGear (i: int) (j: int) (matrix: char array list) =
    if string matrix.[i].[j] <> gear then 
        false 
    else 
        if (countAdjacentNumbers i j matrix) = 2 then
            true 
        else 
            false


let extractNumbersToTheLeft (left: string) (i: int) (j: int) (currentNumber: string) (adjacentNumbers: int list) (matrix: char array list) = 
    let mutable current = currentNumber
    let mutable adjacents = adjacentNumbers

    if numbers |> List.contains left then 
        let mutable current_j = j - 1
        while current_j >= 0 && numbers |> List.contains (string matrix.[i].[current_j]) do 
            current <- String.Concat([current; string matrix.[i].[current_j]])
            current_j <- current_j - 1
        adjacents <- adjacentNumbers |> List.append [current |> Seq.rev |> System.String.Concat |> int]
        current <- ""
    adjacents

let extractNumbersToTheRight (right: string) (i: int) (j: int) (currentNumber: string) (adjacentNumbers: int list) (matrix: char array list) = 
    let mutable current = currentNumber
    let mutable adjacents = adjacentNumbers

    if numbers |> List.contains right then 
        let mutable current_j = j + 1
        while current_j <= matrix.[0].Length - 1 && numbers |> List.contains (string matrix.[i].[current_j]) do 
            current <- String.Concat([current; string matrix.[i].[current_j]])
            current_j <- current_j + 1
        adjacents <- adjacents |> List.append [current |> System.String.Concat |> int]
        current <- ""
    adjacents

let extractStringAboveGear (i: int) (j: int) (matrix: char array list) = 
    let mutable markerJ = j-1
    while markerJ >= 0 && numbers |> List.contains (string matrix.[i-1].[markerJ]) do
        markerJ <- markerJ - 1 
    let mutable stringAboveGear = ""
    markerJ <- markerJ + 1
    while markerJ <= j+1 do 
        stringAboveGear <- String.Concat([stringAboveGear; string matrix.[i-1].[markerJ]])
        markerJ <- markerJ + 1
    if numbers |> List.contains (string matrix.[i-1].[markerJ - 1]) then 
        while markerJ <= matrix.[0].Length - 1 && numbers |> List.contains (string matrix.[i-1].[markerJ]) do
            stringAboveGear <- String.Concat([stringAboveGear; string matrix.[i-1].[markerJ]])
            markerJ <- markerJ + 1
    else 
        ()
    stringAboveGear

let extractStringBelowGear (i: int) (j: int) (matrix: char array list) = 
    let mutable markerJ = j-1
    while markerJ > 0 && numbers |> List.contains (string matrix.[i+1].[markerJ]) do
        markerJ <- markerJ - 1 
    let mutable stringBelowGear = ""
    markerJ <- markerJ + 1
    while markerJ <= j+1 do 
        stringBelowGear <- String.Concat([stringBelowGear; string matrix.[i+1].[markerJ]])
        markerJ <- markerJ + 1
    if numbers |> List.contains (string matrix.[i-1].[markerJ - 1]) then 
        while markerJ <= matrix.[0].Length - 1 && numbers |> List.contains (string matrix.[i+1].[markerJ]) do
            stringBelowGear <- String.Concat([stringBelowGear; string matrix.[i+1].[markerJ]])
            markerJ <- markerJ + 1
    else 
        ()
    stringBelowGear

let extractNumbersFromString (stringAboveGear: string) (adjacentNumbers: int list) = 
    let mutable adjacents = adjacentNumbers

    let charsInStringAbove = stringAboveGear.ToCharArray()
    
    let mutable number = ""

    for char in charsInStringAbove do
        if Char.IsNumber char then 
            number <- String.Concat([number; string char])
        else
            if number <> "" then  
                adjacents <- adjacents |> List.append [int number]
            number <- ""
    if number <> "" then 
        adjacents <- adjacents |> List.append [int number]
    adjacents

let extractAdjacentNumbers (i: int) (j: int) (matrix: char array list) = 
    let mutable adjacentNumbers = []
    
    let left = string matrix.[i].[j-1]
    let right = string matrix.[i].[j+1]

    let mutable currentNumber = ""

    // Links
    adjacentNumbers <- adjacentNumbers |> List.append (matrix |> extractNumbersToTheLeft left i j currentNumber adjacentNumbers)
    // Rechts
    adjacentNumbers <- adjacentNumbers |> List.append (matrix |> extractNumbersToTheRight right i j currentNumber adjacentNumbers)

    // Oben 
    // Idee: 
    // Positioniere dich auf das Feld links ueber dem Gear.
    // Laufe solange nach links, bis Du entweder am Rand bist oder keine Zahl mehr findest.
    // Laufe bis auf das Feld oben rechts vom Gear und schreibe mit.
    // Laufe solange nach recht, bis Du entweder am Rand bist oder keine Zahl mehr findest und schreibe mit. 
    // Extrahiere aus dem Mitschrieb alle Zahlen. 
    // Fuege diese Zahlen der List adjacentNumbers hinzu.

    // Den String ueber dem Gear extrahieren. 
    let stringAboveGear = matrix |> extractStringAboveGear i j
    // Die Zahlen aus dem stringAboveGear extrahieren.
    adjacentNumbers <- adjacentNumbers |> List.append (extractNumbersFromString stringAboveGear adjacentNumbers)
    

    // Unten 
    // Gleiche Idee, nur unter dem Gear.

    // Den String unter dem Gear extrahieren. 
    let stringBelowGear = matrix |> extractStringBelowGear i j
    // Die Zahlen aus dem stringBelowGear extrahieren.
    adjacentNumbers <- adjacentNumbers |> List.append (extractNumbersFromString stringBelowGear adjacentNumbers)

    for number in adjacentNumbers do
        printfn "%i" number

    adjacentNumbers

let calculateGearRatio (matrix: char array list) (i: int) (j: int) = 
    let adjacentNumbers = matrix |> extractAdjacentNumbers i j 
    adjacentNumbers.[0] * adjacentNumbers.[1]

let sumAllGearRatios (matrix: char array list) =
    let mutable sumOfGearRatios = 0
    
    for i in 0..matrix.Length - 1 do 
        for j in 0..matrix.[0].Length - 1 do 
            if matrix |> isGear i j then 
                // printfn "Gear found at (%i, %i)" (i+1) (j+1)
                let gearRatio = calculateGearRatio matrix i j
                printfn "%i" gearRatio
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