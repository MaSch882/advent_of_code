open System 
open System.IO

type SimpleAlmanac = 
    {
        Seeds: list<Int64>
        SeedToSoilMap: list<list<Int64>>
        SoilToFertilizerMap: list<list<Int64>>
        FertilizerToWaterMap: list<list<Int64>>
        WaterToLightMap: list<list<Int64>>
        LightToTemperatureMap: list<list<Int64>>
        TemperatureToHumidityMap: list<list<Int64>>
        HumidityToLocationMap: list<list<Int64>>
    }

type BigAlmanac = 
    {
        LowerSeedBoundA: int64
        SeedRangeA: int64        
        LowerSeedBoundB: int64
        SeedRangeB: int64

        SeedToSoilMap: list<list<Int64>>
        SoilToFertilizerMap: list<list<Int64>>
        FertilizerToWaterMap: list<list<Int64>>
        WaterToLightMap: list<list<Int64>>
        LightToTemperatureMap: list<list<Int64>>
        TemperatureToHumidityMap: list<list<Int64>>
        HumidityToLocationMap: list<list<Int64>>
    }

type Mapper = 
    {
        LowerBound: Int64
        UpperBound: Int64
        Offset: Int64
    }

module SimpleAlmanac =
    let fromData (seeds: list<Int64>) (seedSoil: list<list<Int64>>) (soilFert: list<list<Int64>>) (fertWater: list<list<Int64>>) (waterLight: list<list<Int64>>) (lightTemp: list<list<Int64>>) (tempHum: list<list<Int64>>) (humLoc: list<list<Int64>>)=
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

module BigAlmanac =

    let fromData (lowerBoundA: int64) (rangeA: int64) (lowerBoundB: int64) (rangeB: int64) (seedSoil: list<list<Int64>>) (soilFert: list<list<Int64>>) (fertWater: list<list<Int64>>) (waterLight: list<list<Int64>>) (lightTemp: list<list<Int64>>) (tempHum: list<list<Int64>>) (humLoc: list<list<Int64>>): BigAlmanac = 
        {
            LowerSeedBoundA = lowerBoundA
            SeedRangeA = rangeA
            LowerSeedBoundB = lowerBoundB
            SeedRangeB = rangeB

            SeedToSoilMap = seedSoil
            SoilToFertilizerMap = soilFert
            FertilizerToWaterMap = fertWater
            WaterToLightMap = waterLight
            LightToTemperatureMap = lightTemp
            TemperatureToHumidityMap = tempHum
            HumidityToLocationMap = humLoc
        }

module Mapper = 

    let fromData (src: Int64) (rangeWidth: Int64) (offset: Int64)= 
        {
            LowerBound = src
            UpperBound = src + rangeWidth - 1L
            Offset = offset       
        }

let buildListOfIntegers (index: int) (splitInputMaps: string list list)= 
    splitInputMaps.[index] 
        |> List.skip 1 
        |> List.map (fun s  -> s.Trim()) 
        |> List.map (fun s -> s.Split(" ")) 
        |> List.map (fun str -> str |> Array.toList |> List.map int64)

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

    let seeds = splitInputMaps.[0].[0].Split(":").[1].Trim().Split(" ") |> Array.toList |> List.map int64

    let seedToSoil = splitInputMaps |> buildListOfIntegers 1
    let soilToFertilizer = splitInputMaps |> buildListOfIntegers 2
    let fertilizerToWater = splitInputMaps |> buildListOfIntegers 3
    let waterToLight = splitInputMaps |> buildListOfIntegers 4
    let lightToTemperature = splitInputMaps |> buildListOfIntegers 5
    let temperatureToHumidity = splitInputMaps |> buildListOfIntegers 6
    let humidityToLocation = splitInputMaps |> buildListOfIntegers 7
    
    let almanac = SimpleAlmanac.fromData seeds seedToSoil soilToFertilizer fertilizerToWater waterToLight lightToTemperature temperatureToHumidity humidityToLocation
    almanac

let buildBigAlmanacFromInput (filepath: string) = 
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

    let seedRanges = splitInputMaps.[0].[0].Split(":").[1].Trim().Split(" ") |> Array.toList |> List.map int64
    let lowerBound1 = seedRanges.[0]
    let range1 = seedRanges.[1]
    let lowerBound2 = seedRanges.[2]
    let range2 = seedRanges.[3]

    let seeds = List.append [for i: int64 in 0L..seedRanges.[1] - 1L do lowerBound1 + i] [for i: int64 in 0L..seedRanges.[3] - 1L do lowerBound2 + i]
    
    let seedToSoil = splitInputMaps |> buildListOfIntegers 1
    let soilToFertilizer = splitInputMaps |> buildListOfIntegers 2
    let fertilizerToWater = splitInputMaps |> buildListOfIntegers 3
    let waterToLight = splitInputMaps |> buildListOfIntegers 4
    let lightToTemperature = splitInputMaps |> buildListOfIntegers 5
    let temperatureToHumidity = splitInputMaps |> buildListOfIntegers 6
    let humidityToLocation = splitInputMaps |> buildListOfIntegers 7
    
    let almanac = BigAlmanac.fromData  lowerBound1 range1 lowerBound2 range2 seedToSoil soilToFertilizer fertilizerToWater waterToLight lightToTemperature temperatureToHumidity humidityToLocation
    almanac

let buildMapperFromMapLists (mapList: list<list<Int64>>) = 
    let mutable mapperList = []
    for mapping in mapList do 
        let offset = mapping.[0] - mapping.[1]
        let mapper = Mapper.fromData mapping.[1] mapping.[2] offset
        mapperList <- mapperList |> List.append [mapper]
    mapperList <- mapperList |> List.rev 
    mapperList

let mapAllFromMapList (mapperList: list<Mapper>) (listToMap: list<Int64>) = 
    let mutable mappedSeeds = []
    for seed in listToMap do 
        let mutable needsToBeAppended = true
        for mapper in mapperList do
            if (mapper.LowerBound <= seed) && (seed <= mapper.UpperBound) then
                mappedSeeds <- mappedSeeds |> List.append [seed + mapper.Offset]
                needsToBeAppended <- false 
        if needsToBeAppended then 
            mappedSeeds <- mappedSeeds |> List.append [seed]
            needsToBeAppended <- false
    mappedSeeds <- mappedSeeds |> List.rev
    mappedSeeds

let calculateLowestLocationNumber (almanac: SimpleAlmanac) =
    let seeds = almanac.Seeds
    
    let seedToSoilMapper= almanac.SeedToSoilMap |> buildMapperFromMapLists
    let soilToFertilizerMapper = almanac.SoilToFertilizerMap |> buildMapperFromMapLists
    let fertilizerToWaterMapper = almanac.FertilizerToWaterMap |> buildMapperFromMapLists
    let waterToLightMapper = almanac.WaterToLightMap |> buildMapperFromMapLists
    let lightToTemperatureMapper = almanac.LightToTemperatureMap |> buildMapperFromMapLists
    let temperatureToHumidityMapper = almanac.TemperatureToHumidityMap |> buildMapperFromMapLists
    let humidityToLocationMapper = almanac.HumidityToLocationMap |> buildMapperFromMapLists

    seeds 
        |> mapAllFromMapList seedToSoilMapper 
        |> mapAllFromMapList soilToFertilizerMapper
        |> mapAllFromMapList fertilizerToWaterMapper
        |> mapAllFromMapList waterToLightMapper
        |> mapAllFromMapList lightToTemperatureMapper
        |> mapAllFromMapList temperatureToHumidityMapper
        |> mapAllFromMapList humidityToLocationMapper
        |> List.min

let calculateLowestLocationNumberBigAlmanac (almanac: BigAlmanac) = 
    let seedToSoilMapper= almanac.SeedToSoilMap |> buildMapperFromMapLists
    let soilToFertilizerMapper = almanac.SoilToFertilizerMap |> buildMapperFromMapLists
    let fertilizerToWaterMapper = almanac.FertilizerToWaterMap |> buildMapperFromMapLists
    let waterToLightMapper = almanac.WaterToLightMap |> buildMapperFromMapLists
    let lightToTemperatureMapper = almanac.LightToTemperatureMap |> buildMapperFromMapLists
    let temperatureToHumidityMapper = almanac.TemperatureToHumidityMap |> buildMapperFromMapLists
    let humidityToLocationMapper = almanac.HumidityToLocationMap |> buildMapperFromMapLists

    let lowerSeedBoundA = almanac.LowerSeedBoundA
    let lowerSeedBoundB = almanac.LowerSeedBoundB
    let seedRangeA = almanac.SeedRangeA
    let seedRangeB = almanac.SeedRangeB

    let mutable currentMinimumLocation: int64 = Int64.MaxValue

    for i: int64 in 0L..seedRangeA do
        let seed = lowerSeedBoundA + i
        let location = 
            [seed] 
            |> mapAllFromMapList seedToSoilMapper 
            |> mapAllFromMapList soilToFertilizerMapper
            |> mapAllFromMapList fertilizerToWaterMapper
            |> mapAllFromMapList waterToLightMapper
            |> mapAllFromMapList lightToTemperatureMapper
            |> mapAllFromMapList temperatureToHumidityMapper
            |> mapAllFromMapList humidityToLocationMapper
            |> List.sum
        if location < currentMinimumLocation then
            currentMinimumLocation <- location

    for i: int64 in 0L..seedRangeB do
        let seed = lowerSeedBoundB + i
        let location = 
            [seed] 
            |> mapAllFromMapList seedToSoilMapper 
            |> mapAllFromMapList soilToFertilizerMapper
            |> mapAllFromMapList fertilizerToWaterMapper
            |> mapAllFromMapList waterToLightMapper
            |> mapAllFromMapList lightToTemperatureMapper
            |> mapAllFromMapList temperatureToHumidityMapper
            |> mapAllFromMapList humidityToLocationMapper
            |> List.sum
        if location < currentMinimumLocation then
            currentMinimumLocation <- location

    currentMinimumLocation

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
            let part2 = filepath |> buildBigAlmanacFromInput |> calculateLowestLocationNumberBigAlmanac
            
            printfn "Part 1: %i" part1
            printfn "Part 2: %i" part2

            0
        else    
            printfn "File does not exist!"
            2  