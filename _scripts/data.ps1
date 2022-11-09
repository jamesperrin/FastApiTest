$tcpClient = New-Object System.Net.Sockets.TcpClient("localhost", 80)

$SendData = "GET /api/v1/home HTTP/1.1"
$SendData = "GET / HTTP/1.1"
[byte[]]$sendBytes  = [text.Encoding]::Ascii.GetBytes($SendData)

Write-Host $sendBytes.length
Write-Host $sendBytes

Write-Host "Sending", $tcpClient.Client.Send($sendBytes, $receiveBytes.length)

$receiveBytes = [byte[]]::new(2048)

$receiveLen = $tcpClient.Client.Receive($receiveBytes)

Write-Host $receiveLen
# Out-String [text.Encoding]::UTF8.GetString($receiveBytes, 0, $receiveLen)
# $tcpClient.Close()