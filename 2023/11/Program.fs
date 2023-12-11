open System
open System.IO

type Planet = 
    {
        Id: int
        X: int64 
        Y: int64
    }

module Planet =

    let ToString (planet: Planet) = 
        printfn "Planet %i: (%i, %i)" planet.Id planet.X planet.Y

    let fromData (id: int) (x: int64) (y: int64) = 
        {
            Id = id
            X = x
            Y = y
        }

    let manipulateCoordinates (dx: int64) (dy: int64) (planet: Planet) = 
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
    let mutable indices: int64 list = []

    let lines = filepath |> File.ReadAllLines
    for i in 0..lines.Length - 1 do 
        let line = lines.[i]
        let chars = line.ToCharArray()
        if chars |> Array.forall (fun c -> c = '.') then
            indices <- indices |> List.append [i]

    indices <- indices |> List.rev |> List.map int64
    indices


let calculateIndicesOfEmptyColumns (filepath: string) = 
    let mutable indices: int64 list = []

    let lines = filepath |> File.ReadAllLines
    for i in 0..lines.[0].Length - 1 do
        let mutable isEmpty = true
        for j in 0..lines.Length - 1 do 
            if lines.[j].[i] <> '.' then 
                isEmpty <- false 
        if isEmpty then 
            indices <- indices |> List.append [i]

    indices <- indices |> List.rev |> List.map int64
    indices
    
let expandUniverse (emptyRowIndices: list<int64>) (emptyColumnIndices: list<int64>) (planetsBefore: list<Planet>) = 
    let mutable planetsAfter = []

    for planet in planetsBefore do
        // Spaltenshift
        let yCoordinateBefore = planet.Y
        let mutable yCoordinateShift = 0L

        for i in emptyColumnIndices do 
            if i < yCoordinateBefore then
                yCoordinateShift <- yCoordinateShift + 1L

        // Zeilenshift
        let xCoordinateBefore = planet.X
        let mutable xCoordinateShift = 0L

        for i in emptyRowIndices do 
            if i < xCoordinateBefore then
                xCoordinateShift <- xCoordinateShift + 1L

        let xCoordinateAfter = xCoordinateBefore + xCoordinateShift
        let yCoordinateAfter = yCoordinateBefore + yCoordinateShift
        planetsAfter <- planetsAfter |> List.append [Planet.fromData planet.Id xCoordinateAfter yCoordinateAfter]

    planetsAfter <- planetsAfter |> List.rev

    planetsAfter


let expandUniverseBigBang (emptyRowIndices: list<int64>) (emptyColumnIndices: list<int64>) (planetsBefore: list<Planet>) =
    let mutable planetsAfter = []
    let offset = 999999L
    
    for planet in planetsBefore do
        // Spaltenshift
        let yCoordinateBefore = planet.Y
        let mutable yCoordinateShift: int64 = 0

        for i in emptyColumnIndices do 
            if i < yCoordinateBefore then
                yCoordinateShift <- yCoordinateShift + offset

        // Zeilenshift
        let xCoordinateBefore = planet.X
        let mutable xCoordinateShift: int64 = 0

        for i in emptyRowIndices do 
            if i < xCoordinateBefore then
                xCoordinateShift <- xCoordinateShift + offset

        let xCoordinateAfter = xCoordinateBefore + xCoordinateShift
        let yCoordinateAfter = yCoordinateBefore + yCoordinateShift
        planetsAfter <- planetsAfter |> List.append [Planet.fromData planet.Id xCoordinateAfter yCoordinateAfter]

    planetsAfter <- planetsAfter |> List.rev

    planetsAfter

    
let calculateShortestDistance (planet1: Planet) (planet2: Planet) =
    let l1 = abs (planet1.X - planet2.X) + abs (planet1.Y - planet2.Y)
    l1


let sumShortestPaths (planets: list<Planet>) = 
    let mutable sumOfShortestPaths: int64 = 0
    for planet1 in planets do
        for planet2 in planets do
            sumOfShortestPaths <- sumOfShortestPaths + calculateShortestDistance planet1 planet2
    sumOfShortestPaths <- sumOfShortestPaths / 2L
    sumOfShortestPaths


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
            let emptyRowIndices = filepath |> calculateIndicesOfEmptyRows |> List.map int64
            let emptyColumnIndices = filepath |> calculateIndicesOfEmptyColumns |> List.map int64
            let expandedPlanets = planets |> expandUniverse emptyRowIndices emptyColumnIndices
            let expandedPlanetsBigBang = planets |> expandUniverseBigBang emptyRowIndices emptyColumnIndices

            let part1 = expandedPlanets |> sumShortestPaths
            let part2 = expandedPlanetsBigBang  |> sumShortestPaths
            printfn "Part 1: %i" part1
            printfn "Part 2: %i" part2 
            0
        else    
            printfn "File does not exist!"
            2  