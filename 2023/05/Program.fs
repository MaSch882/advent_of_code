open System 
open System.IO

type Almanac = 
    {
        Seeds: list<int>
        SeedToSoilMap: list<list<int>>
        SoilToFertilizerMap: list<list<int>>
        FertilizerToWaterMap: list<list<int>>
        WaterToLightMap: list<list<int>>
        LightToTemperatureMap: list<list<int>>
        TemperatureToHumidityMap: list<list<int>>
        HumidityToLocationMap: list<list<int>>
    }

type Mapper = 
    {
        SourceRange: list<int>
        Offset: int
    }

module Almanac =
    let fromData (seeds: list<int>) (seedSoil: list<list<int>>) (soilFert: list<list<int>>) (fertWater: list<list<int>>) (waterLight: list<list<int>>) (lightTemp: list<list<int>>) (tempHum: list<list<int>>) (humLoc: list<list<int>>)=
        {
            Seeds = seeds
            SeedToSoilMap = seedSoil
            SoilToFertilizerMap = soilFert
            FertilizerToWaterMap = fertWater
            WaterToLightMap = waterLight
            LightToTemperatureMap = lightTemp
            TemperatureToHumidityMap = tempHum
            HumidityToLocationMap = humLoc
        }
        
module Mapper = 

    let fromData (sourceRange: list<int>) (offset: int) = 
        {
            SourceRange = sourceRange
            Offset = offset       
        }

let buildListOfIntegers (index: int) (splitInputMaps: string list list)= 
    splitInputMaps.[index] 
        |> List.skip 1 
        |> List.map (fun s  -> s.Trim()) 
        |> List.map (fun s -> s.Split(" ")) 
        |> List.map (fun str -> str |> Array.toList |> List.map int)

let buildAlmanacFromInput (filepath: string) = 
    let input = filepath |> File.ReadAllLines

    let mutable splitInputMaps = []

    let mutable currentBlock = []
    for line in input do         
        if line <> "" && line <> "END" then 
            currentBlock <- currentBlock |> List.append [line]
        else 
            splitInputMaps <- splitInputMaps |> List.append [currentBlock |> List.rev]
            currentBlock <- []
    splitInputMaps <- splitInputMaps |> List.rev

    let seeds = splitInputMaps.[0].[0].Split(":").[1].Trim().Split(" ") |> Array.toList |> List.map int

    let seedToSoil = splitInputMaps |> buildListOfIntegers 1
    let soilToFertilizer = splitInputMaps |> buildListOfIntegers 2
    let fertilizerToWater = splitInputMaps |> buildListOfIntegers 3
    let waterToLight = splitInputMaps |> buildListOfIntegers 4
    let lightToTemperature = splitInputMaps |> buildListOfIntegers 5
    let temperatureToHumidity = splitInputMaps |> buildListOfIntegers 6
    let humidityToLocation = splitInputMaps |> buildListOfIntegers 7
    
    let almanac = Almanac.fromData seeds seedToSoil soilToFertilizer fertilizerToWater waterToLight lightToTemperature temperatureToHumidity humidityToLocation
    almanac
    

let buildMapperFromMapLists (mapList: list<list<int>>) = 
    let mutable mapperList = []
    for mapping in mapList do 
        let sourceRange = [for i in 0..mapping.[2]-1 do mapping.[1]+i]
        let offset = mapping.[0] - mapping.[1]
        let mapper = Mapper.fromData sourceRange offset
        mapperList <- mapperList |> List.append [mapper]
    mapperList

let mapAllFromMapList (mapperList: list<Mapper>) (listToMap: list<int>) = 
    let mutable mappedSeeds = []
    for seed in listToMap do 
        let mutable needsToBeAppended = true
        for mapper in mapperList do
            if mapper.SourceRange |> List.contains seed then
                mappedSeeds <- mappedSeeds |> List.append [seed + mapper.Offset]
                needsToBeAppended <- false 
            if needsToBeAppended then 
                mappedSeeds <- mappedSeeds |> List.append [seed]
                needsToBeAppended <- false
    mappedSeeds <- mappedSeeds |> List.rev
    mappedSeeds

let calculateLowestLocationNumber (almanac: Almanac) =
    let seeds = almanac.Seeds
    
    // Seed To Soil
    let mutable seedMapper= almanac.SeedToSoilMap |> buildMapperFromMapLists 
    let mappedSeeds = seeds |> mapAllFromMapList seedMapper

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

            let part1 = filepath |> buildAlmanacFromInput |> calculateLowestLocationNumber
            
            printfn "Part 1: %i" part1
            printfn "Part 2: %i" -1

            0
        else    
            printfn "File does not exist!"
            2  