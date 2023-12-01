open System
open System.IO


let decodeInputToCalibrationValue (input: string) =
    let charArray = input.ToCharArray() |> Array.filter (Char.IsNumber)

    let first : string = string(charArray.GetValue 0)
    let last: string = string(charArray.GetValue (charArray.Length - 1))

    let resultAsString: string = first + last
    // printfn "%s" resultAsString
    int(resultAsString)


let decodeInputToCalibrationValueWithWords (input:string) =
    0




let processAllInputs (filepath: string)  =
    let rows = File.ReadAllLines filepath
    let mutable sum = 0
    rows 
    // |> Array.map decodeInputToCalibrationValue
    |> Array.map decodeInputToCalibrationValueWithWords
    |> Array.sum


[<EntryPoint>]
let main argv = 
    if argv.Length = 1 then 
        let filePath = argv.[0]
        if File.Exists filePath then
            printfn "Processing %s" filePath
            let result = processAllInputs filePath
            
            printfn "%i" result
            0
        else    
            printfn "File does not exist!"
            2    
    else 
        printfn "Please specify a file!"
        1
