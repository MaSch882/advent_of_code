open System
open System.IO

let numbers = ["0";"1"; "2"; "3"; "4"; "5"; "6"; "7"; "8"; "9"]
let delimiter = "."

let buildMatrixFromInput (filepath: string) =
    let lines = filepath |> File.ReadAllLines |> Seq.toList |> List.map (fun line -> line.ToCharArray()) |> Seq.toList

    // for i in 0..lines.Length - 1 do 
    //     for j in 0..9 do
    //         printfn "%c " lines.[i].[j]
    //     printfn "Ende Zeile"

    0

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
            let matrix = filepath |> buildMatrixFromInput 
            0
        else    
            printfn "File does not exist!"
            2   