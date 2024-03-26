import React, { useState } from 'react';
import { Sidebar, SubMenu, Menu, MenuItem } from 'react-pro-sidebar';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { useAuth } from 'AuthContext';
// icons
import { FiChevronsLeft, FiChevronsRight, FiLogIn, FiLogOut } from 'react-icons/fi';
import { FaUpload, FaChalkboardTeacher } from 'react-icons/fa';
import { IoSettingsSharp, IoInformationCircleOutline } from "react-icons/io5";
import { MdOutlineMailOutline } from "react-icons/md";
import { TbLetterS } from "react-icons/tb";

import 'assets/global.css';

function LeftSidebar({ onCollapsedChange }) {
  const navigate = useNavigate();
  const { pathname: currentPath } = useLocation()
  const [collapsed, setCollapsed] = useState(false);
  const [toggled, setToggled] = useState(false);

  const { isLoggedIn, logout } = useAuth();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  const handleCollapsedChange = () => {
    setCollapsed(!collapsed);
    onCollapsedChange(!collapsed);
  };
  const handleHomeClick = () => {
    navigate("/upload");
  };
  const handleToggleSidebar = (value) => {
    setToggled(value);
  };

  return (
    <div className='sidebar-div'>
      <Sidebar
        className={`app ${toggled ? "toggled" : ""}`}
        style={{ height: "100%", position: "fixed", display: "inline-block" }}
        collapsed={collapsed}
        toggled={toggled}
        handleToggleSidebar={handleToggleSidebar}
        handleCollapsedChange={handleCollapsedChange}
      >
        <main>
          <Menu>
            {collapsed ? (
              <MenuItem
                icon={<FiChevronsRight />}
                onClick={handleCollapsedChange}
              ></MenuItem>
            ) : (
              <MenuItem
                suffix={
                  <div className="icon-wrapper" onClick={handleCollapsedChange}>
                    <FiChevronsLeft />
                  </div>}
                className="menu-item"
              >
                <div className="title" onClick={handleHomeClick} >PYTHON TUTOR</div>
              </MenuItem>
            )}
            <hr />
          </Menu>

          <Menu>
            <MenuItem icon={<FaUpload size={18} />} component={<Link to="/upload" />}>Upload project</MenuItem>
            <SubMenu defaultOpen={currentPath.startsWith("/proj")} label={"Practice"} icon={<FaChalkboardTeacher size={22} />}>
              <MenuItem icon={<TbLetterS size={19} />} component={<Link to="/proj4" />} >Scrabble</MenuItem>
              <MenuItem icon={<MdOutlineMailOutline size={20} />} component={<Link to="/proj8" />} >Email Queue</MenuItem>
            </SubMenu>
          </Menu>
          <Menu>
            <MenuItem icon={<IoInformationCircleOutline size={24} />} component={<Link to="/about" />}>About</MenuItem>
          </Menu>

          <Menu>
            <div className="menu-bottom">
              {isLoggedIn ? (
                <>
                  <MenuItem icon={<IoSettingsSharp size={20} />} component={<Link to="/settings" />}> &nbsp;&nbsp; Settings</MenuItem>
                  <MenuItem icon={<FiLogOut size={20} />} onClick={handleLogout}> &nbsp;&nbsp; Logout</MenuItem>
                </>
              ) : (
                <MenuItem icon={<FiLogIn size={20} />} component={<Link to="/login" />}>&nbsp;&nbsp; Login</MenuItem>
              )}
            </div>
          </Menu>
        </main>
      </Sidebar>
    </div>
  );
}
export default LeftSidebar;
