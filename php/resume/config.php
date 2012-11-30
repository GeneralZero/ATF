<?
// Enter your personal details here to build your online resume.

// Let's start with some basic info.  You must include your full name, but if you don't want to include your phone number or email address you can just delete those lines entirely.
$personal['first_name']= 'Brian';
$personal['last_name'] = 'Ridings';
$personal['phone_number'] = '201-6756882';
$personal['email_address'] = 'bridings@stevens.edu';

// Now let's add any social media pages you've created and want to share.  You can add whatever you want by following the format below.  The first item you add is the name of the social media site, and the second item you add is the URL to your page.
$social_media[] = array('Git Hub', 'https://github.com/GeneralZero');
$social_media[] = array('Twitter', 'https://twitter.com/GeneralZer0');

// Cool.  With that stuff out of the way, let's input your work history.  This part requires a bit more information but it's similar to adding a social media page like you did above but with more information.  The first item you enter is last year you worked at the job (or the range of time, if you prefer).  The second item is your job title, the third is the company you worked for, and the fourth is a description of the work you did there.  The description can get a little long, but that's okay.  Just be sure not to use any single quotes ('') or things will break!  You can add as many jobs as you like and the script will adapt.
$work_history[] = array('Sept 2012 - Dec 2012',
						'IT Helpdesk Intern',
						'MacKay Shields LLC',
						'Provided support during the move of the Company to a new buliding.
Created Ghost image of the Computers.');
$work_history[] = array('March 2012',
						'Member of Stevens Cyber Defence Team',
						'NECCDC {Franklin, MA}',
						'Protected Servers and clients from attacks from Red Team.
Configured and Secured services including DNS, LDAP, HTTP, HTTPS, FTP, SMTP, POP.
Dealt with real life situations including configuring VPN, server crashes, hardware failures, password audits, fishing attacks, blocking sites, removing banners, vulnerability scanning, DNSSEC, implementing IPv6.');
$work_history[] = array('January 2012 - July 2012',
						'Computer Intern',
						'WB Engineers | Consultants {NY, NY}',
						'Redesigned and maintained PHP modules for Intranet.
Developed Deltek Dashboard Reports for princables in MDX.
Implemented Archibus Database software.');
$work_history[] = array('June 2011 - Present',
						'Help Desk Information Technology Consultants (ITC)',
						'Stevens Institute of Technology {Hoboken, NJ}',
						'Diagnose computer and network problems for Stevens students, faculty and staff');
$work_history[] = array('June 2011 - Present',
						'Help Desk Information Technology Consultants (ITC)',
						'Stevens Institute of Technology {Hoboken, NJ}',
						'Diagnose computer and network problems for Stevens students, faculty and staff');
// Phew!  That was the hard part.  Now we need to enter in some other important information about you.  Let's start with your education.  You only need to enter two things: your school and a description of your degree.  If you went to Brown University you'd enter that for your school, then put your year and graduation date as the description (e.g. "BA in Social Sciences, Class of 2002").
$education[] = array('Stevens Inisitute of Technology', 'Master: Cyber Security | Major: Computer Science | Minor: Math');
$education[] = array('Don Bosco Prepatory HS', 'High School Deploma');

// Presumably you learned something in school and developed a few skills over the course of your lifetime.  Let's add them here.  
$skills[] = array('Programing Languages', 'Python | C | C# | PHP | Java');
$skills[] = array('Operating Systems', 'Linux | Linux Server | Windows XP/2003/Vista/7');
$skills[] = array('Services', 'Samba | LDAP | Apache | nginx');

// Finally, let's list any awards or honors you've received so you can show off your accomplishments.  To add an award, just use the format below.  (I'm sure you have the hang of this by now, but we're going to go over it anyway.)  The first item you enter is the name of the award/honor (e.g. "Advertising Gold Award" or "Published in the New Yorker") and the second item is the description of the award/honor (e.g. "2010 TV Ads Under $50,000" or "Short story about the trials of Orthodox Jews in Arkansas, May 2016").
$awards[] = array('Award Name', 'Description');
$awards[] = array('Award Name', 'Description');
$awards[] = array('Award Name', 'Description');

// Want to turn off any of the sections on your resume?  You can do that in the settings.  Just change any section from true to false and it'll disappear.  (Note: You can't turn off your work history--that's sort of important!)
$settings['social_media'] = true;
$settings['education'] = true;
$settings['skills'] = true;
$settings['awards'] = false;#true;

// There are also a few other settings you can toggle on and off, such as offering a printable version of your resume and whether to use a dark or light style (set style to "dark" or "light" to choose).
$settings['printable'] = false;#true;
$settings['style'] = "dark";
$settings['lang'] = "en";
?>
