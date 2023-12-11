open System
open System.IO

type Planet = 
    {
        Id: int
        X: int 
        Y: int
    }

module Planet =

    let ToString (planet: Planet) = 
        printfn "Planet %i: (%i, %i)" planet.Id planet.X planet.Y

    let fromData (id: int) (x: int) (y: int) = 
        {
            Id = id
            X = x
            Y = y
        }

    let manipulateCoordinates (dx: int) (dy: int) (planet: Planet) = 
        {
            Id = planet.Id
            X = planet.X + dx
            Y = planet.Y + dy
        }

let buildPlanetsFromInput (filepath: string) = 
    let mutable planets = []

    let lines = filepath |> File.ReadAllLines
    for i in 0..lines.Length-1 do
        let chars = lines.[i].ToCharArray()
        for j in 0..chars.Length-1 do
            if chars.[j] = '#' then 
                planets <- planets |> List.append [Planet.fromData (planets.Length+1) i j]

    planets <- planets |> List.rev
    planets


let calculateIndicesOfEmptyRows (filepath: string) = 
    let mutable indices = []

    let lines = filepath |> File.ReadAllLines
    for i in 0..lines.Length - 1 do 
        let line = lines.[i]
        let chars = line.ToCharArray()
        if chars |> Array.forall (fun c -> c = '.') then
            indices <- indices |> List.append [i]

    indices <- indices |> List.rev
    indices


let calculateIndicesOfEmptyColumns (filepath: string) = 
    let mutable indices = []

    let lines = filepath |> File.ReadAllLines
    for i in 0..lines.[0].Length - 1 do
        let mutable isEmpty = true
        for j in 0..lines.Length - 1 do 
            if lines.[j].[i] <> '.' then 
                isEmpty <- false 
        if isEmpty then 
            indices <- indices |> List.append [i]

    indices <- indices |> List.rev
    indices
    



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

            let planets = filepath |> buildPlanetsFromInput
            let emptyRowIndices = filepath |> calculateIndicesOfEmptyRows
            let emptyColumnIndices = filepath |> calculateIndicesOfEmptyColumns

            let part1 = -1
            let part2 = -1
            printfn "Part 1: %i" part1
            printfn "Part 2: %i" part2 
            0
        else    
            printfn "File does not exist!"
            2  