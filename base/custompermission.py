from rest_framework.permissions import BasePermission,SAFE_METHODS

class custom_permission_data(BasePermission):
    def has_permission(self, request, view):
        print(request.user.role,"------")
        user=request.user
        if request.method=="GET":
            if user.role=="Student":
                return False
            return True
            
        if request.method =='POST':
            if user.role in ['Teacher','Principal']:
                return True
            return False

        if request.method in ['PUT','PATCH']:
            if user.role=="Principal":
                return True
            return False
        
        if request.method=="DELETE":
            if user.role=="Admin":
                return True
            return False
        return super().has_permission(request, view)
    

class custom_permission2(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Object-level permission method.
        
        This method checks if the requesting user has the necessary permissions
        to interact with a specific Attendance object.

        Args:
            request: The HTTP request instance.
            view: The DRF view instance handling the request.
            obj: The Attendance model instance being accessed.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
         
        user = request.user
        print('obj----',obj)
        print('user_Data-------',user)

        # 1. Safe methods (GET, HEAD, OPTIONS) are allowed with restrictions
        if request.method in SAFE_METHODS:
            # If the user is a Student, they can only view their own attendance record
            if user.role == 'Student' and obj.user_Data != user:
                return False
            # Other roles (Teacher, Principal, Admin) can view any attendance record
            return True
        
        # 2. Update methods (PUT, PATCH) are allowed with specific conditions
        if request.method in ['PUT', 'PATCH']:
            # Principals can update any attendance record
            if user.role == 'Principal':
                return True
            
            # Users can update their own attendance record
            if obj.user_Data == user:
                return True
            
            # Other roles (e.g., other Students) are not allowed to update
            return False

        # 3. Delete method is allowed with specific conditions
        if request.method == 'DELETE':

            # Admins can delete any attendance record
            if user.role == 'Admin':
                return True
            
            # Users can delete their own attendance record
            if obj.user_Data == user:
                return True
            # Other roles (e.g., other Students) are not allowed to delete
            return False
        
        # 4. Default denial if none of the conditions are met
        return False