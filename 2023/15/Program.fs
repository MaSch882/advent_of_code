open System 
open System.IO

let calculateHashedValue (input: string) : int =
    let asciiCodes = input |> Seq.map int |> Seq.toList
    let mutable currentValue = 0

    for asciiCode in asciiCodes do
        currentValue <- currentValue |> (+) asciiCode |> (*) 17
        currentValue <- currentValue % 256

    currentValue


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

            printfn "Hash test: %i" ("HASH" |> calculateHashedValue)

            let part1 = -1
            let part2 = -1
            
            printfn "Part 1: %i" part1
            printfn "Part 2: %i" part2

            0
        else    
            printfn "File does not exist!"
            2  