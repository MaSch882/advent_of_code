open System
open System.IO

type Race = 
    {
        Duration: int
        Record: int
    }

module Race = 

    let fromData (d: int) (r: int) =
        {
            Duration = d
            Record = r
        }

    let toString (race: Race) = 
        printfn "Duration: %i; Record: %i" race.Duration race.Record

let buildRaces (filepath: string) : list<Race> = 
    let input = filepath |> File.ReadAllLines

    let durations =
        input.[0].Split(":").[1].Trim().Split(" ") 
        |> Array.map (fun s -> s.Trim()) 
        |> Array.filter (fun s -> s <> "") 
        |> Array.toList
        |> List.map int

    let records = 
        input.[1].Split(":").[1].Trim().Split(" ") 
        |> Array.map (fun s -> s.Trim()) 
        |> Array.filter (fun s -> s <> "") 
        |> Array.toList
        |> List.map int

    let mutable races = []

    for i in 0..durations.Length - 1 do 
        races <- races |> List.append [Race.fromData durations.[i] records.[i]]
    races <- races |> List.rev

    races

let multiplyNumberOfWins (races: list<Race>) = 
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

            let part1 = filepath |> buildRaces |> multiplyNumberOfWins
            let part2 = -1
            
            printfn "Part 1: %i" part1
            printfn "Part 2: %i" part2

            0
        else    
            printfn "File does not exist!"
            2 