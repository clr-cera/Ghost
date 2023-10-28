{ pkgs ? import <nixpkgs> {} }:

let
    my-python-packages = ps: with ps; [ 
      (#SpeechRecognition
        buildPythonPackage rec {
          pname = "SpeechRecognition";
          version = "3.10.0";
          src = fetchPypi {
            inherit pname version;
            sha256 = "sha256-FBMRVeiougDq0be5saL6cchF5Ntfml9mozob1sVcbDU=";
          };
          doCheck = false;
          propagatedBuildInputs = [
            pkgs.python3Packages.requests
          ];
        }
      )
      #Text to Speech functions inside python
      pyttsx3
      
      #For SpeechRecognition to work properly
      pyaudio
      
      
    ];
  in

pkgs.mkShell {
  name = "Ghost"

  nativeBuildInputs = with pkgs.buildPackages; [
    (pkgs.python3.withPackages my-python-packages)
    pkgs.arcanPackages.espeak # For ghost to be able to speak
    pkgs.flac
  ]; 
}
