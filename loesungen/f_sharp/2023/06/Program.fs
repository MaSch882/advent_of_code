open System
open System.IO

type Race = 
    {
        Duration: int64
        Record: int64
    }

module Race = 

    let fromData (d: int64) (r: int64) =
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
        |> List.map int64

    let records = 
        input.[1].Split(":").[1].Trim().Split(" ") 
        |> Array.map (fun s -> s.Trim()) 
        |> Array.filter (fun s -> s <> "") 
        |> Array.toList
        |> List.map int64

    let mutable races = []

    for i in 0..durations.Length - 1 do 
        races <- races |> List.append [Race.fromData durations.[i] records.[i]]
    races <- races |> List.rev

    races

let multiplyNumberOfWins (races: list<Race>) = 
    let mutable product = 1

    for race in races do 
        let duration = race.Duration
        let record = race.Record

        let mutable numberOfWaysToWin = 0

        for i: int64 in 0L..duration do
            let speed = i 
            let driveTime = duration - i 

            let travelledDistance = driveTime * speed

            if travelledDistance > record then 
                numberOfWaysToWin <- numberOfWaysToWin + 1
        
        product <- product * numberOfWaysToWin
    product

let buildRaceFromConcatenatedInput (filepath: string) : list<Race> =
    let input = filepath |> File.ReadAllLines

    let duration =
        input.[0].Split(":").[1].Trim().Split(" ") 
        |> Array.filter (fun s -> s <> "") 
        |> Array.map int64 
        |> Array.sum

    let record =
        input.[1].Split(":").[1].Trim().Split(" ") 
        |> Array.filter (fun s -> s <> "") 
        |> Array.map int64 
        |> Array.sum

    [Race.fromData duration record]


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
            let part2 = filepath |> buildRaceFromConcatenatedInput |> multiplyNumberOfWins
            
            printfn "Part 1: %i" part1
            printfn "Part 2: %i" part2

            0
        else    
            printfn "File does not exist!"
            2 