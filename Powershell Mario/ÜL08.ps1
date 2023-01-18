function ringi_pindala
{
     <#
    .SYNOPSIS
        Arvutab ringi pindala raadiusega
    .DESCRIPTION
        Arvutab ringi pindala raadiusega
    .EXAMPLE
        ring_pindala(8)
    #>
    param($raadius)
    
    $s=[Math]::PI+[Math]::Pow($raadius,2)
    [Math]::Round($s,2)


}

ringi_pindala(4)


function puhtad_nimed
{
    <#
    .SYNOPSIS
        Puhastab nimed
    .DESCRIPTION
        Puhastab nimed lisab suured algustähed teeb ülejaanud vaikseks ja asendab täpitähed
    .EXAMPLE
        puhtad_nimed("        ÖÄÜÕ       ")
    #>
    param($nimi)
    $nimi = $nimi.Trim()
    $nimi = $nimi.replace("Õ","o").replace("Ü","U").replace("Ö","o").replace("Ä","A")
    $puhas = (Get-Culture ).TextInfo.ToTitleCase($nimi.ToLower())



    $puhas
}

puhtad_nimed("     ÕÄÖÜ     ")


    