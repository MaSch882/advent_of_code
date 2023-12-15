open System 
open System.IO


let buildStringsFromInput (filepath: string) = 
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

            let input = filepath |> buildStringsFromInput |> Array.toList

            let part1 = input |> sumAllHashValuesOfStrings
            let part2 = -1
            
            printfn "Part 1: %i" part1
            printfn "Part 2: %i" part2

            0
        else    
            printfn "File does not exist!"
            2  