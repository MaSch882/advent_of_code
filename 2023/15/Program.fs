open System 
open System.IO

type Lens =
    {
        Label: string
        Length: int
    }

module Lens = 

    let fromData (label: string) (length: int) = 
        {
            Label = label
            Length = length
        }

    let toString (lens: Lens) = 
        let lensAsString =  "" + lens.Label + " " + (lens.Length |> string)
        lensAsString

let buildInitializationSequence (filepath: string) = 
    let input = filepath |> File.ReadAllLines
    let strings = input.[0].Split(",")
    strings

let calculateHashedValue (input: string) : int =
    let asciiCodes = input |> Seq.map int |> Seq.toList
    let mutable currentValue = 0

    for asciiCode in asciiCodes do
        currentValue <- currentValue |> (+) asciiCode |> (*) 17
        currentValue <- currentValue % 256

    currentValue

let sumAllHashValuesOfStrings (initializationSequence: list<string>) = 
    initializationSequence |> List.map calculateHashedValue |> List.sum


let buildHashmapFromInitializationSequence (initializationSequence: list<string>) =
    let hashmap: array<array<Lens>> = [| for i in 0..255 do [||] |]

    for command in initializationSequence do
        // command = "="
        if (command.ToCharArray() |> Array.contains '=') then 
            let label = command.Split("=").[0]
            let focalLength = command.Split("=").[1] |> int

            let lens = Lens.fromData label focalLength

            // Wohin wird gehasht?
            let boxNumber = label |> calculateHashedValue 

            // Bereits gehashte Werte holen.
            let boxToUse = hashmap.[boxNumber]
            // Existiert bereits der gehashte Wert?
            let existsLensLabelInBoxToUse = (boxToUse |> Array.filter (fun lens -> lens.Label = label)).Length >= 1
            if existsLensLabelInBoxToUse then
                // Ersetze die alte durch die neue Linse.
                let index = boxToUse |> Array.findIndex (fun lens -> lens.Label = label) 
                boxToUse.[index] <- lens
            // Haenge die Linse an.
            else
                hashmap.[boxNumber] <- boxToUse |> Array.insertAt (boxToUse.Length) lens 

        // command = "-"
        else    
            let label = command.Split("-").[0]

            // Wo soll geloescht werden?
            let boxNumber = label |> calculateHashedValue 
            // Bereits gehashte Werte holen.
            let boxToUse = hashmap.[boxNumber]
            
            let existsLensLabelInBoxToUse = (boxToUse |> Array.filter (fun lens -> lens.Label = label)).Length >= 1
            if existsLensLabelInBoxToUse then 
                let index = boxToUse |> Array.findIndex (fun lens -> lens.Label = label)
                hashmap.[boxNumber] <- boxToUse |> Array.removeAt index

    hashmap

let visualizeHashmap (hashmap: array<array<Lens>>) = 
    printfn "---"
    for i in 0..hashmap.Length - 1 do
        if not (hashmap.[i] |> Array.isEmpty) then
            printf "Box %i: " i 
            for lens in hashmap.[i] do
                printf "[%s]" (lens |> Lens.toString)
            printfn ""
    printfn "---"



let sumFocusingPower (hashmap : array<array<Lens>> ) =
    let mutable sum = 0
    
    for i in 0..hashmap.Length - 1 do 

        let box = hashmap.[i]

        let mutable tempSum = 0
        for j in 0..box.Length- 1 do
            tempSum <- tempSum + (i+1) * (j+1) * box.[j].Length
        sum <- sum + tempSum

    sum

let fileIsGivenAndExists (arguments: String array) (filepath: string) = 
    arguments.Length = 1 && File.Exists filepath

[<EntryPoint>]
let main (argv: String array) = 
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

            let initializationSequence = filepath |> buildInitializationSequence |> Array.toList
            let hashmap = initializationSequence |> buildHashmapFromInitializationSequence

            // hashmap |> visualizeHashmap 

            let part1 = initializationSequence |> sumAllHashValuesOfStrings
            let part2 = initializationSequence |> buildHashmapFromInitializationSequence |> sumFocusingPower
            
            printfn "Part 1: %i" part1
            printfn "Part 2: %i" part2

            0
        else    
            printfn "File does not exist!"
            2  