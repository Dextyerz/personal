local Player = game.Players.LocalPlayer    
local Http = game:GetService("HttpService")
local TPS = game:GetService("TeleportService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local eventShopData = require(ReplicatedStorage.Data.EventShopData)

local Api = "https://games.roblox.com/v1/games/"
local PlaceId, CurrentJobId = game.PlaceId, game.JobId
local ServerAPI = Api .. PlaceId .. "/servers/Public?sortOrder=Desc&limit=100"

-- Cache untuk server yang pernah dicoba
local cacheFile = "ServerCache.json"
local triedServers = {}

if isfile and isfile(cacheFile) then
    local ok, result = pcall(function()
        return Http:JSONDecode(readfile(cacheFile))
    end)
    if ok and type(result) == "table" then
        triedServers = result
    end
end

triedServers[CurrentJobId] = true

local function saveCache()
    if writefile then
        pcall(function()
            writefile(cacheFile, Http:JSONEncode(triedServers))
        end)
    end
end

local function ListServers(cursor)
    local raw = game:HttpGet(ServerAPI .. ((cursor and "&cursor=" .. cursor) or ""))
    return Http:JSONDecode(raw)
end

-- Fungsi utama
task.spawn(function()
    while true do
        local stockChance = eventShopData["Candy Blossom"] and eventShopData["Candy Blossom"].StockChance or 0
        if stockChance > 0 then
            warn("✅ StockChance ditemukan:", stockChance)
            break
        end

        -- Inject ulang script saat teleport
        queue_on_teleport([[loadstring(game:HttpGetAsync("https://raw.githubusercontent.com/Dextyerz/personal/refs/heads/main/asda.lua"))()]])

        local cursor = nil
        local cursorCount = 0
        local maxCursor = 3

        repeat
            cursorCount += 1
            local success, result = pcall(ListServers, cursor)
            if success and result and result.data then
                for _, server in ipairs(result.data) do
                    if server.playing < server.maxPlayers and not triedServers[server.id] then
                        triedServers[server.id] = true
                        saveCache()

                        warn("🔁 Teleporting ke server:", server.id)
                        local ok, err = pcall(TPS.TeleportToPlaceInstance, TPS, PlaceId, server.id, Player)
                        if ok then return end
                        warn("❌ Gagal teleport:", err)
                    end
                end
                cursor = result.nextPageCursor
                task.wait(0.5)
            else
                warn("❌ Gagal ambil server list.")
                break
            end
        until not cursor or cursorCount >= maxCursor

        warn("🔁 Server tidak ditemukan dalam 3 halaman, coba lagi dalam 5 detik...")
        task.wait(5)
    end
end)
