open System
open System.IO

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

            let part1 = -1
            let part2 = -1
            printfn "Part 1: %i" part1
            printfn "Part 2: %i" part2 
            0
        else    
            printfn "File does not exist!"
            2  