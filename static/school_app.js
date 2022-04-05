function delete_teacher(button)
{
    if (window.confirm("Wollen Sie die/den Lehrer*in wirklich löschen?"))
    {
        button.form.submit(this);
    }
}

function delete_department_manager(button)
{
    if (window.confirm("Wollen Sie das die/den Abteilungsvorstand/-ständin wirklich löschen?"))
    {
        button.form.submit(this);
    }
}

function delete_group_of_teachers(button)
{
    if (window.confirm("Wollen Sie die Lehrergruppe wirklich löschen?"))
    {
        button.form.submit(this);
    }
}

function delete_teacher_in_group(button)
{
    if (window.confirm("Wollen Sie das Item wirklich löschen?"))
    {
        button.form.submit(this);
    }
}