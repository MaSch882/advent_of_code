open System 
open System.IO

let calculateLowestLocationOfSeeds (filepath: string) = 
    let input = filepath |> File.ReadAllLines

    let mutable splitInputMaps = []

    let mutable currentBlock = []
    for line in input do         
        if line <> "" then 
            currentBlock <- currentBlock |> List.append [line]
        else 
            splitInputMaps <- splitInputMaps |> List.append [currentBlock |> List.rev]
            currentBlock <- []
    splitInputMaps <- splitInputMaps |> List.rev
    
    


    for list in splitInputMaps do
        for s in list do
            printfn "%s" s
        printfn "----------------------"

    -2

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

            let part1 = filepath |> calculateLowestLocationOfSeeds
            
            printfn "Part 1: %i" part1
            printfn "Part 2: %i" -1

            0
        else    
            printfn "File does not exist!"
            2  