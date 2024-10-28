import java.util.ArrayList;
import java.util.Scanner;

class Course {
    String name;
    int hours;

    Course(String name, int hours) {
        this.name = name;
        this.hours = hours;
    }

    @Override
    public String toString() {
        return "Курс: " + name + ", Часы: " + hours;
    }
}

class Teacher {
    String fullName;
    int age;
    ArrayList<Course> courses;

    Teacher(String fullName, int age) {
        this.fullName = fullName;
        this.age = age;
        this.courses = new ArrayList<>();
    }

    void addCourse(Course course) {
        courses.add(course);
    }

    void removeCourse(Course course) {
        courses.remove(course);
    }

    @Override
    public String toString() {
        return "Преподаватель: " + fullName + ", Возраст: " + age + ", Курсы: " + courses;
    }
}

public class Main {
    static ArrayList<Teacher> teachers = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("\n1. Добавить преподавателя");
            System.out.println("2. Добавить курс к преподавателю");
            System.out.println("3. Удалить курс у преподавателя");
            System.out.println("4. Показать всех преподавателей и их курсы");
            System.out.println("5. Показать курсы отдельно");
            System.out.println("6. Показать преподавателей отдельно");
            System.out.println("0. Выход");
            System.out.print("Выберите действие: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // очистка буфера

            switch (choice) {
                case 1:
                    System.out.print("Введите ФИО преподавателя: ");
                    String fullName = scanner.nextLine();
                    System.out.print("Введите возраст преподавателя: ");
                    int age = scanner.nextInt();
                    teachers.add(new Teacher(fullName, age));
                    break;

                case 2:
                    System.out.print("Введите ФИО преподавателя: ");
                    String teacherName = scanner.nextLine();
                    Teacher teacher = findTeacher(teacherName);
                    if (teacher != null) {
                        System.out.print("Введите название курса: ");
                        String courseName = scanner.nextLine();
                        System.out.print("Введите количество часов: ");
                        int hours = scanner.nextInt();
                        teacher.addCourse(new Course(courseName, hours));
                    } else {
                        System.out.println("Преподаватель не найден.");
                    }
                    break;

                case 3:
                    System.out.print("Введите ФИО преподавателя: ");
                    String teacherNameForRemove = scanner.nextLine();
                    Teacher teacherToRemoveCourse = findTeacher(teacherNameForRemove);
                    if (teacherToRemoveCourse != null) {
                        System.out.print("Введите название курса для удаления: ");
                        String courseToRemove = scanner.nextLine();
                        teacherToRemoveCourse.courses.removeIf(course -> course.name.equals(courseToRemove));
                    } else {
                        System.out.println("Преподаватель не найден.");
                    }
                    break;

                case 4:
                    for (Teacher t : teachers) {
                        System.out.println(t);
                    }
                    break;

                case 5:
                    for (Teacher t : teachers) {
                        for (Course c : t.courses) {
                            System.out.println(c);
                        }
                    }
                    break;

                case 6:
                    for (Teacher t : teachers) {
                        System.out.println("Преподаватель: " + t.fullName);
                    }
                    break;

                case 0:
                    System.out.println("Выход из программы.");
                    scanner.close();
                    return;

                default:
                    System.out.println("Неверный выбор. Попробуйте снова.");
            }
        }
    }

    private static Teacher findTeacher(String fullName) {
        for (Teacher teacher : teachers) {
            if (teacher.fullName.equalsIgnoreCase(fullName)) {
                return teacher;
            }
        }
        return null;
    }
}
