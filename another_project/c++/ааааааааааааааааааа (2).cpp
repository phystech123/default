#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_STUDENTS 50
#define MAX_NAME_LENGTH 30

struct Student {
    char name[MAX_NAME_LENGTH];
    int marks[5];
    float sr_ball;
    int student_code;
};


struct Config {
    int maxFileSize;
    int maxMemorySize;
};

struct Config readConfig() {
    struct Config config;
    printf("Введите максимальный размер файла: ");
    scanf("%d", &config.maxFileSize);
    printf("Введите максимальный размер памяти: ");
    scanf("%d", &config.maxMemorySize);
    return config;
}

void addStudent(struct Student* students, int *count) {
    if (*count >= MAX_STUDENTS) {
        printf("Превышено максимальное количество студентов.\n");
        return;
    }

    struct Student new_student;
    printf("Введите имя студента: ");
    scanf("%s", new_student.name);
    printf("Введите оценки студента (5 штук): ");
    for (int i = 0; i < 5; i++) {
    	if (scanf("%d", &new_student.marks[i]) != 1){
    		break;
		}
    }

    int sum = 0;
    for (int i = 0; i < 5; i++) {
        sum += new_student.marks[i];
    }
    new_student.sr_ball = (float)sum / 5.0;
    students[*count] = new_student;
    (*count)++;
	new_student.student_code = *count; // вот тут надо разыменоваывать переменную count
    printf("Студент успешно добавлен.\n");
}

void addStudentsFromFile(struct Student* students, int* count, const char* filename) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        printf("Не удалось открыть файл.\n");
        return;
    }

    while (!feof(file) && *count < MAX_STUDENTS) {
        struct Student new_student;
        fscanf(file, "%s", new_student.name);

        for (int i = 0; i < 5; i++) {
            fscanf(file, "%d", &new_student.marks[i]);
        }

        int sum = 0;
        for (int i = 0; i < 5; i++) {
            sum += new_student.marks[i];
        }
        new_student.sr_ball = (float)sum / 5.0;

        fscanf(file, "%d", &new_student.student_code);

        students[*count] = new_student;
        (*count)++;
    }

    fclose(file);

    printf("Студенты успешно добавлены из файла.\n");
}

void writeStudentsToFile(struct Student* students, int count, const char* filename) {
    FILE* file = fopen(filename, "w");
    if (file == NULL) {
        printf("Не удалось открыть файл для записи.\n");
        return;
    }

    for (int i = 0; i < count; i++) {
        fprintf(file, "%s ", students[i].name);

        for (int j = 0; j < 5; j++) {
            fprintf(file, "%d ", students[i].marks[j]);
        }

        fprintf(file, "%.2f ", students[i].sr_ball);

    }

    fclose(file);

    printf("Информация о студентах успешно записана в файл.\n");
}

void readStudentsFromFile(struct Student* students, int* count, const char* filename) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        printf("Не удалось открыть файл.\n");
        return;
    }

    *count = 0;
    while (!feof(file) && *count < MAX_STUDENTS) {
        struct Student new_student;
        fscanf(file, "%s", new_student.name);

        for (int i = 0; i < 5; i++) {
            fscanf(file, "%d", &new_student.marks[i]);
        }

        fscanf(file, "%f", &new_student.sr_ball);
        students[*count] = new_student;
        (*count)++;
    }

    fclose(file);

    printf("Студенты успешно добавлены из файла.\n");
}

void printStudents(struct Student* students, int count) {
    printf("Список студентов:\n");
    for (int i = 0; i < count; i++) {
        printf("%d. Имя: %s\n", i + 1, students[i].name);
        printf("   Оценки: ");
        for (int j = 0; j < 5; j++) {
            printf("%d ", students[i].marks[j]);
        }
        printf("Средний балл: %.2f ", students[i].sr_ball);
        
        printf("Код студента: %d\n", students[i].student_code);
    }
}

void updateStudent(struct Student* students, int count) {
    int choice;
    printf("Выберите номер студента для обновления: ");
  
    // Проверка на ошибки ввода
    while (scanf("%d", &choice) != 1 || choice <= 0 || choice > count) {
        printf("Неверный выбор. Попробуйте ещё раз: ");
      
        // Очистка буфера ввода
        while (getchar() != '\n');
    }

    printf("Введите новые оценки студента (5 штук): ");
    for (int i = 0; i < 5; i++) {
        scanf("%d", &students[choice - 1].marks[i]);
    }

    int sum = 0;
    for (int i = 0; i < 5; i++) {
        sum += students[choice - 1].marks[i];
    }
    students[choice - 1].sr_ball = (float)sum / 5.0;

    printf("Студент успешно обновлен.\n");
}


void filterStudents(struct Student* students, int count) {
    int choice;
    printf("Выберите фильтр:\n");
    printf("1. По среднему баллу больше заданного значения\n");
    printf("2. По среднему баллу меньше заданного значения\n");
    printf("3. По количеству долгов больше заданного значения\n");
    printf("4. По количеству долгов меньше заданного значения\n");
    printf("5. Вывести информацию о всех студентах на экран\n");
    scanf("%d", &choice);

    float filter_avg;
    int filter_debts;
    printf("Введите значение фильтра: ");
    if (choice == 1 || choice == 2) {
        scanf("%f", &filter_avg);
    } else if (choice == 3 || choice == 4) {
        scanf("%d", &filter_debts);
    }

    switch (choice) {
        case 1:
            printf("Студенты с средним баллом больше %.2f:\n", filter_avg);
            for (int i = 0; i < count; i++) {
                if (students[i].sr_ball > filter_avg) {
                    printf("Имя: %s\n", students[i].name);
                    printf("Средний балл: %.2f\n", students[i].sr_ball);
                    printf("Код студента: %d\n\n", students[i].student_code);
                }
            }
            break;

        case 2:
            printf("Студенты с средним баллом меньше %.2f:\n", filter_avg);
            for (int i = 0; i < count; i++) {
                if (students[i].sr_ball < filter_avg) {
                    printf("Имя: %s\n", students[i].name);
                    printf("Средний балл: %.2f\n", students[i].sr_ball);
                    printf("Код студента: %d\n\n", students[i].student_code);
                }
            }
            break;

        case 3:
            printf("Студенты с количеством долгов больше %d:\n", filter_debts);
            for (int i = 0; i < count; i++) {
                int debts = 0;
                for (int j = 0; j < 5; j++) {
                    if (students[i].marks[j] < 3) {
                        debts++;
                    }
                }
                if (debts > filter_debts) {
                    printf("Имя: %s\n", students[i].name);
                    printf("Количество долгов: %d\n", debts);
                    printf("Средний балл: %.2f\n", students[i].sr_ball);
                    printf("Код студента: %d\n\n", students[i].student_code);
                }
            }
            break;

        case 4:
            printf("Студенты с количеством долгов меньше %d:\n", filter_debts);
            for (int i = 0; i < count; i++) {
                int debts = 0;
                for (int j = 0; j < 5; j++) {
                    if (students[i].marks[j] < 3) {
                        debts++;
                    }
                }
                if (debts < filter_debts) {
                    printf("Имя: %s\n", students[i].name);
                    printf("Количество долгов: %d\n", debts);
                    printf("Средний балл: %.2f\n", students[i].sr_ball);
                    printf("Код студента: %d\n\n", students[i].student_code);
                }
                
            }
            break;

        case 5:
            printStudents(students, count);
            break;

        default:
            printf("Неверный выбор.\n");
            break;
    }
}

void printExcelStudents(struct Student* students, int count) {
    printf("Отличники:\n");
    int count_excel = 0;
    for (int i = 0; i < count; i++) {
        int excel = 1;
        for (int j = 0; j < 5; j++) {
            if (students[i].marks[j] < 5) {
                excel = 0;
                break;
            }
        }
        if (excel == 1) {
            count_excel++;
            printf("%d. Имя: %s\n", count_excel, students[i].name);
        }
    }

    printf("Количество отличников: %d\n", count_excel);
}

int main() {
	
    struct Config config = readConfig();

    struct Student students[MAX_STUDENTS];
    int studentCount = 0;

    while (1) {
        int choice;
        printf("Выберите действие:\n");
        printf("1. Добавить нового студента\n");
        printf("2. Сохранить информацию о студентах в файл\n");
        printf("3. Загрузить информацию о студентах из файла\n");
        printf("4. Загрузить информацию о студенте, введённую вручную\n");
        printf("5. Вывести информацию о студентах на экран\n");
        printf("6. Обновить информацию о студенте\n");
        printf("7. Вывести информацию об отличниках\n");
        printf("0. Выйти из программы\n");

        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addStudent(students, &studentCount);
                break;

            case 2: {
                char filename[100];
                printf("Введите имя файла: ");
                scanf("%s", filename);
                writeStudentsToFile(students, studentCount, filename);
                break;
            }

            case 3: {
                char filename[100];
                printf("Введите имя файла: ");
                scanf("%s", filename);
                readStudentsFromFile(students, &studentCount, filename);
                break;
            }

            case 4:
                addStudent(students, &studentCount);
                break;

            case 5:
                filterStudents(students, studentCount);
                break;

            case 6:
                updateStudent(students, studentCount);
                break;

            case 7:
                printExcelStudents(students, studentCount);
                break;

            case 0:
                exit(0);

            default:
                printf("Неверный выбор.\n");
                break;
        }
    }

    return 0;
}