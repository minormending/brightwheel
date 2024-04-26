class Permission:
    def __init__(self, data):
        self.object_id = data.get("object_id")
        self.name = data.get("name")
        self.description = data.get("description")
        self.permitted_operations = data.get("permitted_operations")


class UserRole:
    def __init__(self, data):
        self.object_id = data.get("object_id")
        self.name = data.get("name")
        self.marketing_name = data.get("marketing_name")
        self.description = data.get("description")
        self.permissions = [
            Permission(permission_data)
            for permission_data in data.get("permissions", [])
        ]


class ProfilePhoto:
    def __init__(self, data):
        self.object_id = data.get("object_id")
        self.image_url = data.get("image_url")
        self.thumbnail_url = data.get("thumbnail_url")
        self.thumbnail_image_url = data.get("thumbnail_image_url")


class SubsidyProvider:
    def __init__(self, data):
        self.type = data.get("type")
        self.location = data.get("location")
        self.username = data.get("username")
        self.agency_url = data.get("agency_url")
        self.provider_id = data.get("provider_id")
        self.provider_shared_secret = data.get("provider_shared_secret")
        self.provider_auth_key = data.get("provider_auth_key")
        self.id = data.get("id")


class StudentProfile:
    def __init__(self, data):
        self.object_id = data.get("object_id")
        self.billing_status = data.get("billing_status")
        self.first_name = data.get("first_name")
        self.last_name = data.get("last_name")
        self.email = data.get("email")
        self.auth_phone_number = data.get("auth_phone_number")
        self.phone_1 = data.get("phone_1")
        self.phone_2 = data.get("phone_2")
        self.profile_photo = (
            ProfilePhoto(data["profile_photo"]) if "profile_photo" in data else None
        )
        self.raw_passcode = data.get("raw_passcode")
        self.user_type = data.get("user_type")
        self.created_at = data.get("created_at")
        self.activated = data.get("activated")
        self.invite_code = data.get("invite_code")
        self.intro_seen = data.get("intro_seen")
        self.demo_user = data.get("demo_user")
        self.homeroom = data.get("homeroom")
        self.allergies = data.get("allergies")
        self.birthday = data.get("birthday")
        self.age_months = data.get("age_months")
        self.medications = data.get("medications")
        self.notes = data.get("notes")
        self.street_1 = data.get("street_1")
        self.street_2 = data.get("street_2")
        self.city = data.get("city")
        self.state = data.get("state")
        self.country = data.get("country")
        self.zip = data.get("zip")
        self.doctor_name = data.get("doctor_name")
        self.doctor_phone = data.get("doctor_phone")
        self.enrollment_status = data.get("enrollment_status")
        self.enrollment_date = data.get("enrollment_date")
        self.enroll_on_start_date = data.get("enroll_on_start_date")
        self.graduation_date = data.get("graduation_date")
        self.gender = data.get("gender")
        self.student_id = data.get("student_id")
        self.immunization_exempt = data.get("immunization_exempt")
        self.immunization_catch_up = data.get("immunization_catch_up")
        self.immunization_notes = data.get("immunization_notes")
        self.food_plan_type = data.get("food_plan_type")
        self.ethnicity = data.get("ethnicity")
        self.race = data.get("race")
        self.enrollment_date_of_first_contact = data.get(
            "enrollment_date_of_first_contact"
        )
        self.enrollment_date_toured = data.get("enrollment_date_toured")
        self.enrollment_date_paperwork_submitted = data.get(
            "enrollment_date_paperwork_submitted"
        )
        self.enrollment_desired_start_date = data.get("enrollment_desired_start_date")
        self.enrollment_start_date = data.get("enrollment_start_date")
        self.enrollment_end_date = data.get("enrollment_end_date")
        self.enrollment_expected_birth_date = data.get("enrollment_expected_birth_date")
        self.enrollment_sibling_attending = data.get("enrollment_sibling_attending")
        self.enrollment_has_subsidy = data.get("enrollment_has_subsidy")
        self.enrollment_subsidy_notes = data.get("enrollment_subsidy_notes")
        self.enrollment_family_income = data.get("enrollment_family_income")
        self.enrollment_notes = data.get("enrollment_notes")
        self.control_tec_id = data.get("control_tec_id")
        self.school_id = data.get("school_id")
        self.time_zone = data.get("time_zone")
        self.schools = [School(school_data) for school_data in data.get("schools", [])]


class School:
    def __init__(self, data):
        self.object_id = data.get("object_id")
        self.apt_number = data.get("apt_number")
        self.are_passcodes_enabled = data.get("are_passcodes_enabled")
        self.city = data.get("city")
        self.country = data.get("country")
        self.hide_absent_students = data.get("hide_absent_students")
        self.name = data.get("name")
        self.legal_name = data.get("legal_name")
        self.owner_id = data.get("owner_id")
        self.owner_email = data.get("owner_email")
        self.state = data.get("state")
        self.street = data.get("street")
        self.zip = data.get("zip")
        self.phone = data.get("phone")
        self.created_at = data.get("created_at")
        self.stripe_id = data.get("stripe_id")
        self.owner_first_name = data.get("owner_first_name")
        self.owner_last_name = data.get("owner_last_name")
        self.street_1 = data.get("street_1")
        self.street_2 = data.get("street_2")
        self.owner_dob = data.get("owner_dob")
        self.stated_student_count = data.get("stated_student_count")
        self.qr_enabled = data.get("qr_enabled")
        self.qr_code_expires = data.get("qr_code_expires")
        self.accepts_credit_cards = data.get("accepts_credit_cards")
        self.enforces_autopay = data.get("enforces_autopay")
        self.accepts_ach = data.get("accepts_ach")
        self.supports_billing = data.get("supports_billing")
        self.ach_fee = data.get("ach_fee")
        self.cc_percentage = data.get("cc_percentage")
        self.cc_processing_fees_enabled = data.get("cc_processing_fees_enabled")
        self.ach_processing_fees_enabled = data.get("ach_processing_fees_enabled")
        self.allows_open_messaging = data.get("allows_open_messaging")
        self.guardian_edit_student_profile_enabled = data.get(
            "guardian_edit_student_profile_enabled"
        )
        self.website = data.get("website")
        self.program_type = data.get("program_type")
        self.program_type_display = data.get("program_type_display")
        self.logo_url = data.get("logo_url")
        self.logo_id = data.get("logo_id")
        self.logo_watermark_enabled = data.get("logo_watermark_enabled")
        self.signatures_required = data.get("signatures_required")
        self.health_screen_enabled = data.get("health_screen_enabled")
        self.student_checkin_health_screen_enabled = data.get(
            "student_checkin_health_screen_enabled"
        )
        self.student_home_health_screen_enabled = data.get(
            "student_home_health_screen_enabled"
        )
        self.staff_health_screen_enabled = data.get("staff_health_screen_enabled")
        self.business_type = data.get("business_type")
        self.ein = data.get("ein")
        self.added_owner_ssn = data.get("added_owner_ssn")
        self.requires_billing_verification = data.get("requires_billing_verification")
        self.required_fields = data.get("required_fields")
        self.required_information_needed_by = data.get("required_information_needed_by")
        self.permits_staff_self_checkin = data.get("permits_staff_self_checkin")
        self.staff_only_enabled_by_default = data.get("staff_only_enabled_by_default")
        self.time_zone = data.get("time_zone")
        self.accepts_partial_payments = data.get("accepts_partial_payments")
        self.uses_new_billing = data.get("uses_new_billing")
        self.verification_status = data.get("verification_status")
        self.accepts_online_payments_status = data.get("accepts_online_payments_status")
        self.checklist_completed = data.get("checklist_completed")
        self.verification_enabled = data.get("verification_enabled")
        self.billing_migrated_at = data.get("billing_migrated_at")
        self.billing_v2_migrated_at = data.get("billing_v2_migrated_at")
        self.billing_v3_migrated_at = data.get("billing_v3_migrated_at")
        self.billing_v3_migration_in_progress = data.get(
            "billing_v3_migration_in_progress"
        )
        self.show_billing_migration = data.get("show_billing_migration")
        self.parent_feed_activities_enabled = data.get("parent_feed_activities_enabled")
        self.late_payment_fees_amount = data.get("late_payment_fees_amount")
        self.late_payment_fees_num_days_past_due = data.get(
            "late_payment_fees_num_days_past_due"
        )
        self.late_payment_fees_num_days_charges_due = data.get(
            "late_payment_fees_num_days_charges_due"
        )
        self.billing_version = data.get("billing_version")
        self.workweek_start_day = data.get("workweek_start_day")
        self.staff_auto_checkout_enabled = data.get("staff_auto_checkout_enabled")
        self.licensed_capacity = data.get("licensed_capacity")
        self.license_number = data.get("license_number")
        self.parent_directory_enabled = data.get("parent_directory_enabled")
        self.control_tec_type = data.get("control_tec_type")
        self.control_tec_location = data.get("control_tec_location")
        self.control_tec_username = data.get("control_tec_username")
        self.control_tec_agency_url = data.get("control_tec_agency_url")
        self.control_tec_provider_id = data.get("control_tec_provider_id")
        self.control_tec_provider_shared_secret = data.get(
            "control_tec_provider_shared_secret"
        )
        self.control_tec_provider_auth_key = data.get("control_tec_provider_auth_key")
        self.subsidy_providers = [
            SubsidyProvider(subsidy_data)
            for subsidy_data in data.get("subsidy_providers", [])
        ]
        self.organization_id = data.get("organization_id")
        self.belongs_to_multisite = data.get("belongs_to_multisite")
        self.ach_fee_type = data.get("ach_fee_type")
        self.ach_fee_percentage = data.get("ach_fee_percentage")
        self.ach_fee_percentage_min = data.get("ach_fee_percentage_min")
        self.ach_fee_percentage_max = data.get("ach_fee_percentage_max")


class Student:
    def __init__(self, data):
        self.relationship_type = data.get("relationship_type")
        self.guardian_id = data.get("guardian_id")
        self.parent_feed_activities_enabled = data.get("parent_feed_activities_enabled")
        self.daily_report_email_enabled = data.get("daily_report_email_enabled")
        self.contact_share_option = data.get("contact_share_option")
        self.student = StudentProfile(data["student"]) if "student" in data else None
