#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char executable_file[100];

    // Prompt the user for the name of the compiled executable to run
    printf("Enter the name of the compiled executable (e.g., program.exe): ");
    scanf("%s", executable_file);

    // Check if the executable has ".exe" extension, add it if not
    if (strstr(executable_file, ".exe") == NULL) {
        strcat(executable_file, ".exe");
    }

    // Run the compiled executable using the system function
    int status = system(executable_file);

    if (status == 0) {
        printf("The program ran successfully.\n");
    } else {
        printf("Error: Failed to run the program.\n");
    }

    return 0;
}