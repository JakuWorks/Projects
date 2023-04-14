# Script made by JakuWorks: kubek0823@gmail.com, https://www.youtube.com/channel/UCetKkeRPmwfGZ1ZAT3V6GTA

Write-Host @'

WARNING! The following installation will reset _it's_ files in C:\Users\[User]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup ||| and in ||| it's \WindowsCustomStartup\RequiredForUpgradedStartup folder if they are already present (installation got repeated).

Note: Repeated installations are supported, but clear the old files. 
'@
Read-Host @'


-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%
-%  PRESS ENTER TO CONTINUE...  -%
-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%
'@


function RemoveIfPresentAndCopyItem() {

    Param(
        [ Parameter( Mandatory = $true ) ] $ToCopy,
        [ Parameter( Mandatory = $true ) ] $Destination,
        [ switch ] [ Parameter ( Mandatory = $false ) ] $ReturnNewPath
    )

    #FINISH THIS FUNCTION (Maybe Write-Host what's happening)

    $LiteralPath = "$Destination\$( $ToCopy.Basename ).$( $ToCopy.Extension )"

    if ( Test-Path -Path $LiteralPath ) {
        Remove-Item -Path $LiteralPath
    }

    # If ReturnNewPath property was toggled on.
    if ( $ReturnNewPath ) { 

        $PassThruOutput = Copy-Item -Path $ToCopy -Destination $Destination -PassThru -Recurse

        $PassThruOutput.mmlkmklkklkmlkmlkmkm

    }

    # If ReturnNewPath property is $null of $false, 0, "", etc. (negative)
    else {

        Copy-Item -Path $ToCopy -Destination $Destination -Recurse

    }

}


# Defining an array of objects with pieces of information about what and where to copy, with an optional Parameter - NewName
$AllItemsToCopy = @(

    [ PsCustomObject ] @{
        ToCopy = '.\Assets\RequiredForUpgradedStartup-ToCopy';
        Destination = '.\';
        NewName = 'RequiredForUpgradedStartup'
    },

    [ PsCustomObject ] @{
        ToCopy = '.\Assets\ThunderbirdToTray';
        Destination = "$env:USERPROFILE\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    }

)


function RevertInstallation() {

    Param (
        [ Parameter( Mandatory = $false) ] $ErrorMessage
    )

    #TODO
    Write-Host $ErrorMessage

}


try {

    for ( $index = 0; $index -lt $AllItemsToCopy.Count; $index++ ) {

        # If a NewName parameter was found
        if ( $AllItemsToCopy[ $index ] | Get-Member 'NewName' ) {
            
            # Check, is .NewName a string.
            if ( $AllItemsToCopy[ $index ].NewName.GetType().Name -eq 'String' ) {
                
                # If it was a String.

                RemoveIfPresentAndCopyItem( -ToCopy $AllItemsToCopy[ $index ].ToCopy -Destination $AllItemsToCopy[ $index ].Destination -ReturnNewPath)

                # Finished here! Finish this, make the upper function return something, make the RevertInstallation function work.

            }

            else {

                # If it wasn't a String.

                RevertInstallation( -ErrorMessage @'
An error has occured!
Found a child of $AllItemsToCopy array of objects, that has a defined NewName property that isn't a String!
'@
                )
                
            }

        } 

        # If no NewName parameter was found.
        else {

            RemoveIfPresentAndCopyItem( -ToCopy $AllItemsToCopy[ $index ].ToCopy -Destination $AllItemsToCopt[ $index ].Destination )

        }

    }
}

catch {

}

# USE THE FUNCTION ON THE FILES ! 

# The ASII art has repeated ` characters, that's why the ASII appears uneven. In the terminal they appear as one.
Write-Host @'




================================================================
 _____                             _ 
/  ___|                           | |
\ ``--. _   _  ___ ___ ___  ___ ___| |
 ``--. \ | | |/ __/ __/ _ \/ __/ __| |
/\__/ / |_| | (_| (_|  __/\__ \__ \_|
\____/ \__,_|\___\___\___||___/___(_)

Successfully installed the files into their proper directories!
'@
Read-Host @'


-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%
-%  PRESS ENTER TO EXIT...  -%
-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%
'@