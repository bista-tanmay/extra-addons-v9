<html>
    <head>
        <style type="text/css">
            ${css}
            .right_table{
                "margin-top: 2px";
            }
        </style>
    </head>
    <body>
        <h1><center>Session Details</center></h1>
        %for session in objects:
            <table class="basic_table" width="100%">
                <tr>
                    <td>
                        <b>${_("Name")}</b>
                    </td>
                    <td>
                        <b>${_("Instructor")}</b>
                    </td>
                    <td>
                        <b>${_("Course")}</b>
                    </td>
                    <td>
                        <b>${_("Seats")}</b>
                    </td>
                    <td>
                        <b>${_("User Email")}</b>
                    </td> 
                    
                </tr>
                <tr>
                    <td>
                        <b>${session.name}</b>
                    </td>
                    <td>
                        <b>${session.instructor_id.name}</b>
                    </td>
                    <td>
                        <b>${session.course_id.name}</b>
                    </td>
                        <td>
                            <b>${session.seats}</b>
                        </td>
                     <td>
                            <b>${get_email(user.id)}</b>
                        </td>
                </tr>
            </table>
            <br/>
            <br/>
            <br/>
            <h1><center>Attendee Details</center></h1>
            <br/>
            <br/>
            <table class="basic_table" width="100%">
                <tr>
                    <td>
                        <b>${_("Name")}</b>
                    </td>
                    <td>
                        <b>${_("partner")}</b>
                    </td>
                </tr>
                %if session.attendee_ids:
                    %for attendee in session.attendee_ids:
                        <tr>
                            <td>
                                ${attendee.name}
                            </td>
                            <td>
                                ${attendee.partner_id.name}
                            </td>
                        </tr>
                    %endfor
               %endif
            </table>
            <p style="page-break-before:always;"/>
     %endfor
    </body>
</html>
