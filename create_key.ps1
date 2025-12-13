$Token = "ya29.a0Aa7pCA-Sgr3dm0ZIzmoVbRSd8lhhdGOk_E8rwcxfLMraoIiqYvtY_ZUt_Dhlsg0213aCgYKARUSARYSFQHGX2MiL" # Truncated for brevity, I will use full token in real exec or via param
$Project = "project-c465bc45-299b-470d-8b6"
$Url = "https://apikeys.googleapis.com/v2/projects/$Project/locations/global/keys"

$Body = @{
    displayName  = "Chat Unrestricted 2025"
    restrictions = @{}
} | ConvertTo-Json

Invoke-RestMethod -Uri $Url -Method Post -Headers @{Authorization = "Bearer $Token" } -Body $Body -ContentType "application/json"
